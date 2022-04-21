from tkinter import *
import matplotlib
import networkx as nx
matplotlib.use("TKAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tracefinal import *
from tokenizer import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TKAgg")
import tkinter as tk

root = Tk()
root.title('Compilers Project')
root.geometry("900x600")

root.wm_attributes('-transparentcolor', '#ab23ff')

def open_win():
   LARGE_FONT = ("verdana", 12)

   class SeaofBTCapp(tk.Tk):
      def __init__(self, *args, **kwargs):
         tk.Tk.__init__(self, *args, **kwargs)

         tk.Tk.wm_title(self, "Tokenization and Tracing")
         tk.Tk.wm_minsize(self, 800, 300)

         container = tk.Frame(self)
         container.pack(side="top", fill="both", expand=True)

         container.grid_rowconfigure(0, weight=1)
         container.grid_columnconfigure(0, weight=1)

         self.frames = {}

         for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
         self.show_frame(StartPage)

         def present():
            self.show_frame(StartPage)

      def show_frame(self, cont):
         frame = self.frames[cont]
         frame.tkraise()

   class StartPage(tk.Frame):
      def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)

         label2 = tk.Label(self, text=tokenizer(T.get()), font = (("Times New Roman"), 15), pady=210, fg="black")
         label2.pack()

         label3 = tk.Label(self, text=tracefinal(T.get()), font=(("Times New Roman"), 15), pady=20, fg="black")
         label3.pack()

         showDFAbutton = Button(self, text='Show DFA', command=lambda: controller.show_frame(PageOne))
         showDFAbutton.pack()



   class PageOne(tk.Frame):
      def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="DFA Diagram", font=LARGE_FONT,fg='green',bg='white')
         label.pack(pady=10, padx=10)


         button1 = tk.Button(self, text="ID Node",fg="#0d28d5",bg="white",
                             activeforeground="#0d28d5",activebackground="white", command=lambda:controller.show_frame(PageTwo))
         button1.pack()

         button2 = tk.Button(self, text="Num Node",fg="#0d28d5",bg="white",activeforeground="#0d28d5",activebackground="white",
                             command=lambda: controller.show_frame(PageThree))
         button2.pack()

         button3 = tk.Button(self, text="Bracket Node",fg="#0d28d5",bg="white",activeforeground="#0d28d5",activebackground="white",
                             command=lambda: controller.show_frame(PageFour))
         button3.pack()

         f = Figure(figsize=(30, 30), dpi=100)
         a = f.add_subplot(111)

         G = nx.DiGraph()
         G.add_node(' ')
         G.add_node('Error')
         G.add_node('other')
         G.add_node('+,-,*,/')
         G.add_node(' +,-,*,/,other')
         G.add_node('+,-,*,/,0 ')
         G.add_node('/')
         G.add_node(' /')
         G.add_node('+,-,*')
         G.add_node('+,-,* ')
         G.add_edges_from([(' ', 1)])

         transition = [(1, 'ID1', 'Identifier'), (1, 'NUM1', '0-9'), (1, 'Bracket', '('), ('ID1', 'OP1', '+,-,*'),
                       ('ID1', 'OP2', '/'), ('NUM1', 'OP1', '+,-,*'), ('NUM1', 'OP2', '/'), ('OP1', 'NUM3', '0-9'),
                       ('OP1', 'ID3', 'Identifier'), ('OP2', 'ID3', 'Identifier'), ('OP2', 'NUM3', '1-9'), ('Bracket', 3, ')'),
                       ('OP1', 'Bracket', '('), ('OP2', 'Bracket', '('), (3, 'OP1', '+,-,*'), (3, 'OP2', '/')]
         for i in transition:
             G.add_edge(i[0], i[1], transition=i[2])

         positions = {'Error': [-3, -6], 'ID1': [-2, -2], 'NUM1': [-2, -4], 'OP1': [0, -2], 'OP2': [0, -4], 'NUM3': [3, -4],
                      'ID3': [3, -2], 'Bracket': [-2, -6], 3: [1, -6], ' ': [-5.1, -4], 1: [-4, -4], 'other': [-1, -6.9],
                      '+,-,*,/': [-3.6, -5.5], ' +,-,*,/,other': [-2.3, -3], '+,-,*,/,0 ': [-2.2, -4.7],
                      ' /': [1.5, -4.3],
                      '/': [2.8, -2.5], '+,-,*': [1.8, -1.7], '+,-,* ': [2.7, -3.4]}

         fixed_nodes = positions.keys()
         pos = nx.spring_layout(G, pos=positions, fixed=fixed_nodes)

         nx.draw(G, pos, with_labels=True, font_size=8, node_size=400, node_color='LightGreen', node_shape='o', ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' ')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('other')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('+,-,*,/')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' +,-,*,/,other')],
                                ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('+,-,*,/,0 ')], ax=a)

         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('+,-,* ')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('+,-,*')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' /')], ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('/')], ax=a)

         nx.draw_networkx_edges(G, pos, edge_color='LightGreen', edgelist=[('OP1', 'Bracket')], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='LightGreen', edgelist=[('OP2', 'Bracket')], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='LightGreen', edgelist=[(3, 'OP1')], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='LightGreen', edgelist=[(3, 'OP2')], width=1, arrowsize=14, ax=a)
         # nx.draw_networkx_edges(G,pos,edge_color='g',edgelist = [(' ',1)] , width=1,arrowsize=14)

         nx.draw_networkx_nodes(G, pos, node_size=200, node_color='LightGreen', node_shape='o', nodelist=[(3)],
                                edgecolors='black', ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=200, node_color='LightGreen', node_shape='o', nodelist=[('ID3')],
                                edgecolors='black', ax=a)
         nx.draw_networkx_nodes(G, pos, node_size=200, node_color='LightGreen', node_shape='o', nodelist=[('NUM3')],
                                edgecolors='black', ax=a)

         nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'transition'), label_pos=0.7,
                                      font_size=8, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='r', connectionstyle='arc3, rad = 0.3', edgelist=[(1, 'Error')], width=1,
                                arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='r', connectionstyle='arc3, rad = 0.5', edgelist=[('OP1', 'Error')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='r', connectionstyle='arc3, rad = 0.4', edgelist=[('OP2', 'Error')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='r', connectionstyle='arc3, rad = -0.5', edgelist=[(3, 'Error')],
                                width=1,
                                arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='b', connectionstyle='arc3, rad = 0.3', edgelist=[('NUM3', 'OP1')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='b', connectionstyle='arc3, rad = -0.3', edgelist=[('NUM3', 'OP2')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='b', connectionstyle='arc3, rad = 0.3', edgelist=[('ID3', 'OP1')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(G, pos, edge_color='b', connectionstyle='arc3, rad = -0.3', edgelist=[('ID3', 'OP2')],
                                width=1, arrowsize=9, ax=a)

         canvas = FigureCanvasTkAgg(f, self)
         # canvas.show()
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

         toolbar = NavigationToolbar2TkAgg(canvas, self)
         toolbar.update()
         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


   class PageTwo(tk.Frame):
      def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Identifier DFA", font=LARGE_FONT)
         label.pack(pady=10, padx=10)

         button1 = tk.Button(self, text="Back to DFA", fg="#0d28d5", bg="white",
                             activeforeground="#0d28d5", activebackground="white",
                             command=lambda: controller.show_frame(PageOne))
         button1.pack()

         f = Figure(figsize=(5, 5), dpi=100)
         a = f.add_subplot(111)

         ID = nx.DiGraph()
         ID.add_node('A-Z,a-z,_,0-9')
         ID.add_node(' ')
         ID.add_edges_from([('A', 'A'), (' ', 'A')])

         transition = [('A', 'Error', ';'), ('A', 'OP1', '*,+,-'), ('A', 'OP2', '/')]
         for i in transition:
            ID.add_edge(i[0], i[1], transition=i[2])

         positions = {'A': [0, 0], 'OP1': [1, 1], 'OP2': [1, -1], 'Error': [0, -1], 'A-Z,a-z,_,0-9': [0, 0.3],
                      ' ': [-0.2, 0]}

         fixed_nodes = positions.keys()
         pos = nx.spring_layout(ID, pos=positions, fixed=fixed_nodes)

         nx.draw(ID, pos, with_labels=True, font_size=8, node_size=400, node_color='violet', node_shape='o', ax=a)
         nx.draw_networkx_nodes(ID, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('A-Z,a-z,_,0-9')],
                                ax=a)
         nx.draw_networkx_nodes(ID, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' ')], ax=a)
         nx.draw_networkx_nodes(ID, pos, node_size=200, node_color='violet', node_shape='o', nodelist=[('A')],
                                edgecolors='black', ax=a)
         nx.draw_networkx_nodes(ID, pos, node_size=500, node_color='LightGreen', node_shape='o', nodelist=[('OP1')],
                                ax=a)
         nx.draw_networkx_nodes(ID, pos, node_size=500, node_color='LightGreen', node_shape='o', nodelist=[('OP2')],
                                ax=a)
         nx.draw_networkx_edges(ID, pos, edge_color='g', edgelist=[(' ', 'A')], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(ID, pos, edge_color='blue', edgelist=[('A', 'OP1')], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(ID, pos, edge_color='blue', edgelist=[('A', 'OP2')], width=1, arrowsize=14, ax=a)

         nx.draw_networkx_edge_labels(ID, pos, edge_labels=nx.get_edge_attributes(ID, 'transition'), label_pos=0.5,
                                      font_size=10, ax=a)
         canvas = FigureCanvasTkAgg(f, self)
         # canvas.show()
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

         toolbar = NavigationToolbar2TkAgg(canvas, self)
         toolbar.update()
         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

   class PageThree(tk.Frame):
         def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Num DFA", font=LARGE_FONT)
            label.pack(pady=10, padx=10)

            button1 = tk.Button(self, text="Back to DFA", fg="#0d28d5", bg="white",
                                activeforeground="#0d28d5", activebackground="white",
                                command=lambda: controller.show_frame(PageOne))
            button1.pack()

            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)

            NUM = nx.DiGraph()
            NUM.add_node('0-9')
            NUM.add_node(' ')
            NUM.add_edges_from([('A', 'A'), (' ', 'A')])

            transition = [('A', 'Error', '-[0-9]'), ('A', 'OP1', '*,+,-'), ('A', 'OP2', '/')]
            for i in transition:
               NUM.add_edge(i[0], i[1], transition=i[2])

            positions = {'A': [0, 0], 'OP1': [1, 1], 'OP2': [1, -1], 'Error': [0, -1], '0-9': [0, 0.3], ' ': [-0.2, 0]}

            fixed_nodes = positions.keys()
            pos = nx.spring_layout(NUM, pos=positions, fixed=fixed_nodes)

            nx.draw(NUM, pos, with_labels=True, font_size=9, node_size=400, node_color='orange', node_shape='o', ax=a)
            nx.draw_networkx_nodes(NUM, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('0-9')], ax=a)
            nx.draw_networkx_nodes(NUM, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' ')], ax=a)
            nx.draw_networkx_nodes(NUM, pos, node_size=200, node_color='orange', node_shape='o', nodelist=[('A')],
                                   edgecolors='black', ax=a)
            nx.draw_networkx_nodes(NUM, pos, node_size=500, node_color='LightGreen', node_shape='o', nodelist=[('OP1')],
                                   ax=a)
            nx.draw_networkx_nodes(NUM, pos, node_size=500, node_color='LightGreen', node_shape='o', nodelist=[('OP2')],
                                   ax=a)
            nx.draw_networkx_edges(NUM, pos, edge_color='g', edgelist=[(' ', 'A')], width=1, arrowsize=14, ax=a)
            nx.draw_networkx_edges(NUM, pos, edge_color='g', edgelist=[('A', 'OP1')], width=1, arrowsize=14, ax=a)
            nx.draw_networkx_edges(NUM, pos, edge_color='g', edgelist=[('A', 'OP2')], width=1, arrowsize=14, ax=a)

            nx.draw_networkx_edge_labels(NUM, pos, edge_labels=nx.get_edge_attributes(NUM, 'transition'), label_pos=0.5,
                                         font_size=9, ax=a)

            canvas = FigureCanvasTkAgg(f, self)
            # canvas.show()
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



   class PageFour(tk.Frame):
      def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         label = tk.Label(self, text="Bracket DFA", font=LARGE_FONT)
         label.pack(pady=10, padx=10)

         button1 = tk.Button(self, text="Back to DFA", fg="#0d28d5", bg="white",
                             activeforeground="#0d28d5", activebackground="white",
                             command=lambda: controller.show_frame(PageOne))
         button1.pack()

         f = Figure(figsize=(5, 5), dpi=100)
         a = f.add_subplot(111)

         B = nx.DiGraph()

         B.add_node(' ')
         B.add_node('Error')
         B.add_node('*,+,-,/')
         B.add_node(' *,+,-,/,0')  # from OP4
         B.add_node('*,+,-,/,other ')  # from OP3
         B.add_node('/')
         B.add_node(' /')  # from NUM4
         B.add_node('*,+,-')
         B.add_node('*,+,- ')  # from NUM4
         B.add_edges_from([(' ', 2)])

         transition = [(2, 'ID2', 'Identifier'), (2, 'NUM2', '0-9'), ('ID2', 'OP3', '*,+,-'), ('ID2', 'OP4', '/'),
                       ('NUM2', 'OP3', '*,+,-'), ('NUM2', 'OP4', '/'), ('OP3', 'NUM4', '0-9'), ('OP3', 'ID4', 'Identifier'),
                       ('OP4', 'ID4', 'Identifier'), ('OP4', 'NUM4', '1-9'), ('ID4', 3, ')'), ('NUM4', 3, ')')]
         for i in transition:
            B.add_edge(i[0], i[1], transition=i[2])

         positions = {'Error': [-3, -6], 'ID2': [-2, -2], 'NUM2': [-2, -4], 'OP3': [0, -2], 'OP4': [0, -4],
                      'ID4': [3, -2],
                      'NUM4': [3, -4], 3: [4, -3], ' ': [-4.1, -3], 2: [-3, -3], 'OP1': [4, -2], 'OP2': [5, -2],
                      'other': [1, -5.5], '*,+,-,/': [-3.2, -5.5], ' *,+,-,/,0': [-0.2, -4.5],
                      '*,+,-,/,other ': [-1.2, -4.7],
                      ' /': [1.5, -4.3], '/': [2.8, -2.5], '*,+,-': [1.8, -1.7], '*,+,- ': [2.7, -3.4]}

         fixed_nodes = positions.keys()
         pos = nx.spring_layout(B, pos=positions, fixed=fixed_nodes)

         nx.draw(B, pos, with_labels=True, font_size=8, node_size=400, node_color='SkyBlue', node_shape='o', ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' ')], ax=a)
         # nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w',node_shape='o',nodelist=[('other')])
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('*,+,-,/')], ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' *,+,-,/,0')], ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('*,+,-,/,other ')],
                                ax=a)

         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('*,+,- ')], ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('*,+,-')], ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[(' /')], ax=a)
         nx.draw_networkx_nodes(B, pos, node_size=500, node_color='w', node_shape='o', nodelist=[('/')], ax=a)

         nx.draw_networkx_edges(B, pos, edge_color='g', edgelist=[('ID4', 3)], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='g', edgelist=[('NUM4', 3)], width=1, arrowsize=14, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='g', edgelist=[(' ', 2)], width=1, arrowsize=14, ax=a)

         nx.draw_networkx_nodes(B, pos, node_size=300, node_color='LightGreen', node_shape='o', nodelist=[(3)],
                                edgecolors='black', ax=a)
         nx.draw_networkx_edge_labels(B, pos, edge_labels=nx.get_edge_attributes(B, 'transition'), label_pos=0.7,
                                      font_size=8, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='r', connectionstyle='arc3, rad = 0.3', edgelist=[(2, 'Error')],
                                width=1,
                                arrowsize=9, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='r', connectionstyle='arc3, rad = -0.2', edgelist=[('OP3', 'Error')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='r', connectionstyle='arc3, rad = -0.3', edgelist=[('OP4', 'Error')],
                                width=1, arrowsize=9, ax=a)
         # nx.draw_networkx_edges(B,pos,edge_color='r',connectionstyle='arc3, rad = -0.5', edgelist = [(3,'Error')] , width=1,arrowsize=9)
         nx.draw_networkx_edges(B, pos, edge_color='b', connectionstyle='arc3, rad = 0.3', edgelist=[('NUM4', 'OP3')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='b', connectionstyle='arc3, rad = -0.3', edgelist=[('NUM4', 'OP4')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='b', connectionstyle='arc3, rad = 0.3', edgelist=[('ID4', 'OP3')],
                                width=1, arrowsize=9, ax=a)
         nx.draw_networkx_edges(B, pos, edge_color='b', connectionstyle='arc3, rad = -0.3', edgelist=[('ID4', 'OP4')],
                                width=1, arrowsize=9, ax=a)

         canvas = FigureCanvasTkAgg(f, self)
         # canvas.show()
         canvas.draw()
         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

         toolbar = NavigationToolbar2TkAgg(canvas, self)
         toolbar.update()
         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


   root = SeaofBTCapp()
   root.mainloop()


bg = PhotoImage(file = "image/background2.png")

background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = Label(text = "Enter your Arithmetic Expression", font=(("Times New Roman"), 17), fg="white", bg = "#122e5a")
label1.place()
label1.pack(pady=150)

button = tk.Button(root, bg="white", text="Submit Arithmetic Expression", font=(("Amaranth"), 10, 'bold'), fg = "black", command=open_win)
button.pack( pady = 10)


T = tk.Entry(root, bg="white", width=20, relief="sunken", font=(("Times New Roman"), 20))
T.pack()
T.place(relx=0.5, rely=0.48, anchor=CENTER)



root.mainloop()
