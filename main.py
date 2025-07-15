from database import create_tables, get_session
from models import User, Address
from sqlalchemy import select

def run():
    create_tables()
    session = get_session()

    # Add records
    user = User(
        name="pallavi",
        fullname="Pallavi Sharma",
        addresses=[Address(email_address="pallavi@example.com")]
    )
    session.add(user)
    session.commit()

    # Query
    stmt = select(User).where(User.name == "pallavi")
    for result in session.scalars(stmt):
        print(result)

    session.close()

if __name__ == "__main__":
    run()
