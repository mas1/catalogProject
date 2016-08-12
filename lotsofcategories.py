from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from catalog_database import Base, Categories, Items

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



category1 = Categories(name="Soccer")

session.add(category1)
session.commit()

categoryItem1 = Items(name="Soccer Ball", description="A ball used to play Soccer",
 category=category1)

session.add(categoryItem1)
session.commit()

category2 = Categories(name="Basketball")

session.add(category2)
session.commit()

categoryItem2 = Items(name="Basketball", description="A ball used to play bball. Bouncy",
 category=category2)

session.add(categoryItem2)
session.commit()

category3 = Categories(name="Football")

session.add(category3)
session.commit()

categoryItem3 = Items(name="Helmet", description="Very protective.",
 category=category3)

 session.add(categoryItem3)
 session.commit()





print "added items!"
