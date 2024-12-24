from manim import *
import numpy as np

from typing import Any

class WeightedLine(Line):
    """A line to display weighted edges in a network graph.

    Parameters
    ----------
    args
        Arguments to be passed to :class:`Line`
    weight
        The weight of the edge to display
    weight_config
        Dict of options to be passed to :class:`Text`
    weight_alpha
        The alpha position on the edge to show the weight
    bg_config
        Dict of options to be passed to :class:`Rectangle`
    add_bg
        Boolean to show a rectangle behind the weight
    kwargs
        Additional arguments to be passed to :class:`Line`

    """

    def __init__(
        self,
        *args: Any,
        weight: str | int | float | None = None,
        weight_config: dict | None = None,
        weight_alpha: float = 0.5,
        bg_config: dict | None = None,
        add_bg: bool = True,
        **kwargs: Any,
    ):
        self.weight = weight
        self.alpha = weight_alpha
        self.add_bg = add_bg
        super().__init__(*args, **kwargs)

        self.weight_config = {
            "color": WHITE,
            "slant": ITALIC,
            "font_size": DEFAULT_FONT_SIZE * 0.5,
        }

        if weight_config:
            self.weight_config.update(weight_config)

        self.bg_config = {
            "color": config.background_color,
            "opacity": 1,
        }
        if bg_config:
            self.bg_config.update(bg_config)

        if self.weight is not None:
            self._add_weight()

    def _add_weight(self):
        """
        Clears any current weight and then displays the weight is not none.

        Use weight_config dict to send options to the Text object.

        Use bg_config dict to send options to the background Rectangle object.

        """

        # Set the new weight if it is present

        point = self.point_from_proportion(self.alpha)
        label = Text(str(self.weight), **self.weight_config)
        label.move_to(point)

        if self.add_bg:
            label.add_background_rectangle(**self.bg_config)
            label.background_rectangle.height += SMALL_BUFF

        self.add(label)


class numbering(Scene):
    def construct(self):
        vertex = [1,2,3,4,5,6,7,8]
        edges = [ (1,2),(1,4),(1,7),
                 (2,3),(2,5),(3,6),
                 (4,2),(4,5),(4,7),
                 (5,3),(5,6),(5,8),
                 (7,5),(7,8),(8,6)]

        layaut = { 1:[-4,0, 0],
                  2:[-2,2, 0],
                  3:[2,2, 0],
                  4:[-2,0,0],
                  5:[2,0,0],
                  6:[4,0,0],
                  7:[-2,-2,0],
                  8:[2,-2,0]}

        edg_cnf = { (1,2): {'weight':6},
                   (1,4): {'weight': 2},
                   (1,7): {'weight': 4},
                   (2,3): {'weight': 4},
                   (2,5): {'weight': 4},
                   (3,6): {'weight': 3},
                   (4,2): {'weight': 3},
                   (4,5): {'weight': 5},
                   (4,7): {'weight': 3},
                   (5,3): {'weight': 2},
                   (5,6): {'weight': 5},
                   (5,8): {'weight': 2},
                   (7,5): {'weight': 3},
                   (7,8): {'weight': 6},
                   (8,6): {'weight': 1} }

        t = Tex("Numbering algorithm", font_size=100)
        self.play(Write(t))
        self.wait(0.5)
        self.play(FadeOut(t))
        print()
        g = DiGraph(vertex, edges, layout=layaut, layout_scale=3,
                    labels=True, edge_type=WeightedLine,
                    edge_config=edg_cnf).shift(UP)
        t1 = IntegerTable(
            [[int(i) for i in range(1,8)], [int(0) for i in range(1,8)]],
            row_labels=[Text("Vertex"), Text("Number")],
            include_outer_lines=True).shift(2*DOWN+[0,-0.5,0]).scale(0.5)

        self.play(Create(g),Create(t1),run_time=5)

        self.wait(1)

        def animateEdges(tupl):
            self.play(*[g.edges[n].animate.set_color(YELLOW_A) for n in tupl],
                      *[AnimationGroup(Indicate(g.edges[n], color=YELLOW_A), lag_ratio=0.7) for n in tupl])
            self.wait(0.5)

        animateEdges([(1,2),(1,4),(1,7)])
        animateEdges([(4,2),(4,5),(4,7)])
        animateEdges([(2,3),(2,5)])
        animateEdges([(7,5),(7,8)])
        animateEdges([(5,3),(5,6),(5,8)])
        animateEdges([(3,6)])
        animateEdges([(8,6)])
        # TODO animar el ultimo vertice 6

        def changeTable(arr):
            return IntegerTable([[int(i) for i in range(1,8)], arr],
                row_labels=[Text("Vertex"), Text("Number")],
                include_outer_lines=True).shift(2*DOWN+[0,-0.5,0]).scale(0.5)

        t2 = changeTable([1,0,0,0,0,0,0])
        t3 = changeTable([1,0,0,2,0,0,0])
        t4 = changeTable([1,3,0,2,0,0,0])
        t5 = changeTable([1,3,0,2,0,0,4])
        t6 = changeTable([1,3,0,2,5,0,4])
        t7 = changeTable([1,3,0,2,5,0,4])

        self.play(Transform(t1,t2))
        animateEdges([(1,2),(1,4),(1,7)])
        g.remove_edges(*[(1,2),(1,4),(1,7)])
        self.wait(0.5)
        self.play(Transform(t2,t3))
        animateEdges([(4,2),(4,5),(4,7)])
        #g.remove_edges(*[(4,2),(4,5),(4,7)])
        g.remove(*[(4,2),(4,5),(4,7)])
        # self.wait(0.5)
        # self.play(Transform(t3,t4))
        # self.wait(0.5)
        # self.play(Transform(t4,t5))
        # self.wait(0.5)
        # self.play(Transform(t5,t6))
        # self.wait(0.5)

        #remove_edges([(1,2),(1,4),(1,7)])

        self.wait(1)


