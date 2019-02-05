import os
import urllib

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))
 

class FileRenamer(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Pretty Simple Renamer")

        self.set_border_width(10)

# Listado de archivos
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)

        hboxFiles = Gtk.Box(spacing=1)
        box_outer.pack_start(hboxFiles, True, True, 0)

        hboxFiles.pack_start(listBoxFolder, True, True, 0)
        hboxFiles.pack_start(listBoxFiles, True, True, 0)
        listBoxFiles.show_all()
        listBoxFolder.show_all()
# Controles
        
# Boton para agregar archivos
        hboxFileButtons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box_outer.pack_start(hboxFileButtons, True, True, 0)
        buttonOpen = Gtk.Button.new_with_label("Agregar Archivo")
        buttonOpen.connect("clicked", self.on_add_clicked)
        hboxFileButtons.pack_start(buttonOpen, True, True, 0)

# Boton para quitar archivos
        buttonRemove = Gtk.Button.new_with_label("Quitar Archivo")
        buttonRemove.connect("clicked", self.on_remove_clicked)
        hboxFileButtons.pack_start(buttonRemove, True, True, 0)        

# Entrada de nombre


        self.entry = Gtk.Entry()
        self.entry.set_text("Nuevo Nombre#")
        box_outer.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        box_outer.pack_start(hbox, True, True, 0)

        textLabel = Gtk.Label()
        textLabel.set_label("# Sera sucedido por numeros ascedentes a partir del que defina")
        textLabel.set_halign(Gtk.Align.END)
        hbox.pack_start(textLabel, True, True, 0)

        adjustment = Gtk.Adjustment(1, 0, 100, 1, 10, 0)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        hbox.pack_start(self.spinbutton, False, False, 0)

# Botones
        button = Gtk.Button.new_with_label("Cambiar nombre")
        button.connect("clicked", self.on_rename_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Cerrar")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)


# Agregar archivos
    def on_add_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Elija un archivo", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            src = dialog.get_filename()
            srcFolder = dialog.get_current_folder() + "/"
            srcFile = src.split(srcFolder,1)

            listBoxFiles.add(ListBoxRowWithData(srcFile[1]))
            listBoxFiles.show_all()

            listBoxFolder.add(ListBoxRowWithData(srcFolder))
            listBoxFolder.show_all()

            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

# Quitar archivos
    def on_remove_clicked(self, button):
        for filename in listBoxFiles:
            srcFileName = filename
            contador = filename.get_index()
            srcFolder = listBoxFolder.get_row_at_index(contador)

            if srcFileName.is_selected() == True:
                index = filename.get_index()
                listBoxFiles.remove(filename)
                listBoxFolder.remove(srcFolder)
                print index

# Renombrar archivos
    def on_rename_clicked(self, button):
        self.renameFiles()

    def renameFiles(self):
        i = self.spinbutton.get_value_as_int()


        for filename in listBoxFiles:
            srcFileName = filename.data
            contador = filename.get_index()
            srcFolder = listBoxFolder.get_row_at_index(contador).data

            extension = srcFileName.split('.',1)
            if len(extension) < 2:
                 dst = srcFolder + self.entry.get_text() + str(i)
            else:
                 dst = srcFolder + self.entry.get_text() + str(i) + '.' + extension[1]
      
#        for filename in directory:
#        for filename in listBoxFiles.get_selected_rows().:
            src = srcFolder + srcFileName

#            print src
            print src + " >>> " + dst

            os.rename(src,dst)
            i +=1 

# Cerrar aplicacion
    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()



# Variables globales
#path = "/home/agustin/Documentos/"
#directory = os.listdir( path )
listBoxFiles = Gtk.ListBox()
listBoxFolder = Gtk.ListBox()

win = FileRenamer()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
