"""
This module contains unit tests for the Label class, verifying creation, update, and deletion of labels,
along with interactions with a mocked user object to simulate system operations.
"""


import unittest
from src import Label, User, ItemDontHaveThisAttribute, NonChangeableProperty
from sqlalchemy.orm import sessionmaker
from src.logic.orms.orm import UserORM, Base, LabelORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import date
from unittest.mock import Mock
class TestLabel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.SessionLocal = sessionmaker(bind=cls.engine)

        cls.session = TestLabel.SessionLocal()

        db_test_user = UserORM(name='Test User', email='test@example.com', password='teste')
        cls.session.add(db_test_user)
        cls.session.commit()

        cls.test_user = User(name=db_test_user.name, id_user=db_test_user.id_user, session=cls.session)

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def setUp(self):
        self.session = TestLabel.SessionLocal()
        self.create_test_items()

    def create_test_items(self):
        db_test_label = LabelORM(name='Test Label', id_user=self.test_user.id_user, color='azul') 
        self.session.add(db_test_label)
        self.session.commit()

        self.test_label = Label(name=db_test_label.name,
                                user=self.test_user,
                                id_label=db_test_label.id_label,
                                color=db_test_label.color,
                                session = self.session)

    def tearDown(self):
        self.session.close()

    def test_init(self) -> None:
        """
        Tests the proper initialization of the Label object, verifying that the name and color attributes are correct.
        """
        self.assertEqual(self.test_label.name, "Test Label")
        self.assertEqual(self.test_label.color, "azul")
                         
    def test_label_save_to_db(self):
        new_label = Label(user=self.test_user, name='New Label', color='verde', session=self.session)
        new_label.save_to_db()

        saved_label = self.session.query(LabelORM).filter_by(name='New Label').first()
        self.assertIsNotNone(saved_label)
        self.assertEqual(saved_label.color, 'verde')


    def test_delete(self) -> None:
        label_id = self.test_label._id_label
        self.test_label.delete()
        
        deleted_label = self.session.query(LabelORM).filter_by(id_label=label_id).first()
        self.assertIsNone(deleted_label)


    def test_update_valid(self) -> None:
        """
        Tests valid update of the Label object by changing its name and color, and verifies that the new values are correct.
        """
        self.test_label.update(name="New Label", color="red")
        self.assertEqual(self.test_label.name, "New Label")
        self.assertEqual(self.test_label.color, "red")

    def test_update_invalid(self) -> None:
        """
        Tests invalid update of the Label object by attempting to update a non-existent attribute and verifies that the correct exception is raised.
        """
        with self.assertRaises(ItemDontHaveThisAttribute):
            self.test_label.update(invalid_property="Invalid")


    def test_update_non_changeable_property(self) -> None:
        """
        Tests that updating a non-changeable property (user) raises the appropriate exception.
        """
        with self.assertRaises(NonChangeableProperty):
            self.test_label.update(user=Mock())


    def test_propertys(self):
        self.assertEqual(self.test_label.user, self.test_user)
        self.assertEqual(self.test_label.name, 'Test Label')
        self.assertEqual(self.test_label.color, 'azul')
        self.assertIsInstance(self.test_label.id_label, int)
        self.assertEqual(self.test_label.id_label, self.test_label._id_label)

            
if __name__ == "__main__":
    unittest.main()