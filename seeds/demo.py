from flask_seeder import Seeder, Faker, generator
from main import Task
from faker import Faker
fake = Faker()

class DemoSeeder(Seeder):
  # run() will be called by Flask-Seeder
  def run(self):
    for i in range(10):
      task = Task(title=fake.job(), content=fake.sentence(10))
      self.db.session.add(task)
      
# Create a new Faker and tell it how to create Task objects
# faker = Faker(
#   cls=Task,
#   init={
#     'title': generator.Name(),
#     'content': generator.Name()
#   }
# )

# for task in faker.create(10):
#   print("Adding task: %s" % task)
#   self.db.session.add(task)
    


