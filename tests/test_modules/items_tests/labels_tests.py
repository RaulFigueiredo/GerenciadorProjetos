import unittest
from unittest.mock import Mock
from src.logic.items.label import Label
from src.gui.label_create import AddLabelDialog
from src.gui.label_edit import EditLabelDialog
from unittest.mock import patch
import tkinter as tk


class TestLabel(unittest.TestCase):

    def setUp(self):
        self.mock_user = Mock()
        self.label = Label(self.mock_user, "Test Label", "blue")

    def test_init(self):
        self.assertEqual(self.label.name, "Test Label")
        self.assertEqual(self.label.color, "blue")
        self.mock_user.add_label.assert_called_with(self.label)

    def test_delete(self):

        self.label.delete()
        self.mock_user.remove_label.assert_called_with(self.label)

    def test_update_valid(self):

        self.label.update(name="New Label", color="red")
        self.assertEqual(self.label.name, "New Label")
        self.assertEqual(self.label.color, "red")
        self.mock_user.update_label.assert_called_with(self.label)

    def test_update_invalid(self):

        with self.assertRaises(ValueError):
            self.label.update(task="New Task")

class TestAddLabelDialog(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.add_label_dialog = AddLabelDialog(self.root)
        self.add_label_dialog.top.withdraw()  

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertIsNone(self.add_label_dialog.resultado)
        self.assertEqual(self.add_label_dialog.nome_entry.get(), "")
        self.assertEqual(self.add_label_dialog.cor_combobox.get(), "")

    @patch('tkinter.Toplevel.destroy')
    def test_on_confirm(self, mock_destroy):

        self.add_label_dialog.nome_entry.insert(0, "Test Label")
        self.add_label_dialog.cor_combobox.set("blue")
        self.add_label_dialog.on_confirm()

        self.assertEqual(self.add_label_dialog.resultado, ("Test Label", "blue"))
        mock_destroy.assert_called_once()

    def test_show(self):
        with patch.object(self.add_label_dialog.top, 'wait_window', return_value=None):
            resultado = self.add_label_dialog.show()
        self.assertIsNone(resultado)  

class TestEditLabelDialog(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.edit_label_dialog = EditLabelDialog(self.root, "Nome Anterior", "blue")
        self.edit_label_dialog.top.withdraw()  

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.edit_label_dialog.nome_entry.get(), "Nome Anterior")
        self.assertEqual(self.edit_label_dialog.cor_combobox.get(), "blue")

    @patch('tkinter.messagebox.showwarning')
    @patch('tkinter.Toplevel.destroy')
    def test_on_confirm_valid(self, mock_destroy, mock_showwarning):
        self.edit_label_dialog.nome_entry.delete(0, tk.END)
        self.edit_label_dialog.nome_entry.insert(0, "Novo Nome")
        self.edit_label_dialog.cor_combobox.set("green")
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_not_called()
        self.assertEqual(self.edit_label_dialog.resultado, ("Novo Nome", "green"))
        mock_destroy.assert_called_once()

    @patch('tkinter.messagebox.showwarning')
    def test_on_confirm_empty_nome(self, mock_showwarning):
        self.edit_label_dialog.nome_entry.delete(0, tk.END)
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_called_once_with("Aviso", "O nome da etiqueta não pode estar vazio.", parent=self.edit_label_dialog.top)
        self.assertIsNone(self.edit_label_dialog.resultado)

    @patch('tkinter.messagebox.showwarning')
    def test_on_confirm_empty_cor(self, mock_showwarning):
        self.edit_label_dialog.cor_combobox.set('')
        self.edit_label_dialog.on_confirm()

        mock_showwarning.assert_called_once_with("Aviso", "Por favor, selecione uma cor.", parent=self.edit_label_dialog.top)
        self.assertIsNone(self.edit_label_dialog.resultado)

    def test_show(self):
        with patch.object(self.edit_label_dialog.top, 'wait_window', return_value=None):
            resultado = self.edit_label_dialog.show()
        self.assertIsNone(resultado)  


if __name__ == '__main__':
    unittest.main()