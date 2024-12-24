from manim import *
import random


class scenePrueba(Scene):
    def construct(self):
        vercies = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        edges = [(1,6), (2,6), (2,7), (3,8), (3, 9), (4, 7), (5, 6), (5, 9)]

        vc = {'radius':0.2}
        g = Graph(vercies, edges,layout="shell", vertex_config=vc)
        self.play(Create(g))
        self.wait(0.5)
        g[1].set_color(BLUE)

        def prueba(graph,vert,color, tupl):
            for n in vert:
                g[n].set_color(color)
            self.play(*[g.edges[n].animate.set_color(color) for n in tupl],
                    *[Flash(graph.vertices[n], color=color, flash_radius=0.3) for n in vert],
                    *[AnimationGroup(Indicate(graph.vertices[n], color=color), lag_ratio=0.7) for n in vert])
            self.play(*[g.edges[n].animate.set_color(WHITE) for n in tupl])

        prueba(g,[6],RED,[(1,6)])

        self.wait(0.5)
        prueba(g,[2,5],BLUE,[(2,6),(5,6)])
        self.wait(0.5)
        # 1 2 5 
        # 7 9
        prueba(g,[7,9],RED,[(2,7),(5,9)])
        self.wait(0.5)
        # 7 9
        # 4 3
        prueba(g, [3,4],BLUE,[(4, 7),(3, 9)])
        self.wait(0.5)
        prueba(g,[8], RED, [(3, 8)])

        self.play(
            g.animate.change_layout({
                1:[-2,2, 0],
                2:[-2,1, 0],
                3:[-2,0, 0],
                4:[-2,-1,0],
                5:[-2,-2,0],
                6:[2,1.5,0],
                7:[2,0.5,0],
                8:[2,-0.5,0],
                9:[2,-1.5,0]
            })
        )
        self.wait(0.5)






