import time
import json
import requests
import pprint
import textwrap

hosts = 'localhost'
port = 8998

headers = {
  'Content-Type': 'application/json'
}

s = requests.Session()
s.headers = headers

"""
操作Apache Livy
"""

def create_session():
    url = "http://{}:{}/sessions".format(hosts, port)
    data = dict()
    data["kind"] = "spark"
    r = s.post(url, data = json.dumps(data))
    return r.json()


def get_all_session():
    url = "http://{}:{}/sessions".format(hosts, port)
    sessions_json = s.get(url).json()
    sessions_total = sessions_json["total"]
    sessions = list()

    for session in sessions_json["sessions"]:
        sessions.append(session["id"])

    assert(sessions_total == len(sessions))

    return sessions


def delete_session(session):
    url = "http://{}:{}/sessions/{}".format(hosts, port, session)
    r = s.delete(url)
    return r.json()


def execute_statement(session):
    url = "http://{}:{}/sessions/{}/statements".format(hosts, port, session)

    '''
    data = {
        'code': textwrap.dedent("""
            spark.catalog.dropTempView("tmp_date")
            val df = Seq(("06-03-2009"),("07-24-2009")).toDF("date")
            val tmp = df.select(col("date"),to_date(col("date"),"MM-dd-yyyy").as("to_date"))
            val tempView = tmp.createTempView("tmp_date")
            val d = spark.sql("SELECT date,to_date FROM tmp_date")
            val result = d.collect().map(_.toSeq)
            %table result
        """)
    }
    '''

    data = {
        'code': textwrap.dedent("""
            import scala.collection.mutable
            spark.catalog.dropTempView("tmp_date")
            val df = Seq(("06-03-2009"),("07-24-2009")).toDF("date")
            val tmp = df.select(col("date"),to_date(col("date"),"MM-dd-yyyy").as("to_date"))
            val tempView = tmp.createTempView("tmp_date")
            val d = spark.sql("SELECT date,to_date FROM tmp_date")
            val result = d.collect().map(t => {
                val map: mutable.Map[String, Any] = mutable.HashMap()
                val schema = t.schema

                for (i <- 0 until schema.size) {
                    map += (schema.names(i) -> t.get(i))
                }
                map
           })
           %table result
        """)
    }

    # data = {
    #     'code': textwrap.dedent("""
    #         val x = List(List(1, "a", "2019-04-02"), List(3, "b", "2019-05-01"))
    #         %table x
    #     """)
    # }
    r = s.post(url, data = json.dumps(data))
    return r.json()


def get_statement_result(session, statement):
    url = "http://{}:{}/sessions/{}/statements/{}".format(hosts, port, session, statement)
    r = s.get(url)
    return r.json()


if __name__ == '__main__':
    """
    r = delete_session(1)
    print(r)

    session_json = create_session()
    print(session_json)
    """

    sessions_id = get_all_session()
    print(sessions_id)

    statement_json = execute_statement(sessions_id[0])
    pprint.pprint(statement_json)

    while True:
        time.sleep(1)
        statement_result = get_statement_result(sessions_id[0], statement_json["id"])
        status = statement_result["state"]

        print("-> session[{}] statement[{}] state[{}]".format(sessions_id[0], statement_json["id"], status))
        if(status == "available"):
            break

    pprint.pprint(statement_result)
