from blog.app import create_app, db

app = create_app()

#
# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")


# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
#     from blog.models import User
#     admin = User(username="admin", password=generate_password_hash("admin"), is_staff=True)
#     james = User(username="james", password=generate_password_hash("james"))
#     db.session.add(admin)
#     db.session.add(james)
#     db.session.commit()
#     print("done! created users:", admin, james)


# @app.cli.command("create-articles")
# def create_articles():
#     """
#     Run in your terminal:
#     flask create-articles
#     > done! created articles: <Article #1 'Travel in India'> <Article #2 'Football match'>
#     """
#     from blog.models import Article
#     travel = Article(title="Travel in India", text="Text text text")
#     football = Article(title="Football match", text="Text text text")
#     db.session.add(travel)
#     db.session.add(football)
#     db.session.commit()
#     print("done! created users:", travel, football)