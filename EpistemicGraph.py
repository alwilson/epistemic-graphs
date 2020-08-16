#!/usr/bin/env python3

from graphviz import Digraph

class EG:
    green='forestgreen'
    red='firebrick3'

    def __init__(self, name, format_str, dark=False):
        self.arg_name = 'A'
        self.dark = dark
        self.format_str = format_str

        # neato could be useful for heavier graphs
        self.graph = Digraph(name, filename=name, format=format_str, engine='dot')
        self.graph.attr(ratio='0.2') # for dot
        #self.graph.attr(overlap='false', sep='+1') # for neato
        self.graph.attr(rankdir='BT')
        if self.format_str != 'svg':
            self.graph.attr(dpi='300')

        self.graph.attr('node', shape='box', style='rounded')

        if dark:
            self.graph.attr(bgcolor='gray15', fontcolor='white')
            self.graph.attr('node', fontcolor='white')

    def incr_chr(self, c):
        return chr(ord(c) + 1) if c != 'Z' else 'A'

    def incr_str(self, s):
        lpart = s.rstrip('Z')
        num_replacements = len(s) - len(lpart)
        new_s = lpart[:-1] + self.incr_chr(lpart[-1]) if lpart else 'A'
        new_s += 'A' * num_replacements
        return new_s

    def link(self, side, A, B):
        arg_color = 'white' if self.dark else 'black'
        if side == 'for':
            arg_color = EG.green
        elif side == 'against':
            arg_color = EG.red

        self.graph.edge(A, B, color=arg_color)

    def node(self, side, arg_str, conns, primary=False, url=''):
        arg_color = 'white' if self.dark else 'black'
        if side == 'for':
            arg_color = EG.green
        elif side == 'against':
            arg_color = EG.red

        rank = 'source' if primary else 'sink'
        if self.format_str == 'svg' and url != '':
            self.graph.node(self.arg_name, f'{self.arg_name} = {arg_str}\n(click for link)', color=arg_color, rank=rank, URL=url)
        else:
            if url != '':
                self.graph.node(self.arg_name, f'{self.arg_name} = {arg_str}\n(see footnotes)', color=arg_color, rank=rank)
                print(f'{self.arg_name}: {url}')
            else:
                self.graph.node(self.arg_name, f'{self.arg_name} = {arg_str}', color=arg_color, rank=rank)

        for c in conns:
            self.graph.edge(self.arg_name, c, color=arg_color)

        return_name = self.arg_name
        self.arg_name = self.incr_str(self.arg_name)
        return return_name

    def finish(self, title_str):
        self.graph.attr(label=title_str)

        #f.view()
        self.graph.render()
