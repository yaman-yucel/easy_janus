from collections.abc import Generator
from contextlib import contextmanager

from gremlin_python.driver import serializer
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import GraphTraversalSource

# Make sure that janusgraph server is started at 8182


@contextmanager
def connect() -> Generator[GraphTraversalSource, None, None]:
    """Context manager for handling JanusGraph connections."""
    connection = None
    try:
        connection = DriverRemoteConnection(url="ws://localhost:8182/gremlin", traversal_source="g", message_serializer=serializer.GraphSONSerializersV3d0())
        g = traversal().withRemote(connection)
        yield g
    finally:
        if connection:
            connection.close()


# add a vertex
with connect() as g:
    vertex = g.addV("Hercules_GOD")
    vertex.property("name", "hercules").property("age", 25).iterate()
    vertex = g.addV("Hades_GOD")
    vertex.property("name", "Hades").property("age", 1000).iterate()

# check vertex value
with connect() as g:
    hercules_age = g.V().has("name", "hercules").values("age").next()
    print(f"Hercules is {hercules_age} years old.")

# add edge
with connect() as g:
    g.V().hasLabel("Hercules_GOD").as_("s").V().hasLabel("Hades_GOD").as_("t").addE("is_friend").from_("s").to("t").iterate()

with connect() as g:
    print(g.V().toList())
    print(g.E().toList())

    print(g.V().valueMap().toList())
    print(g.E().valueMap().toList())
# drop all graph
with connect() as g:
    g.V().drop().iterate()
