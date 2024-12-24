from manim import *




class discreteProbability(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(z_range=[0,0.5,0.1])
        #lab = ax.get_z_axis_label(Tex("$z$-label"))
        #self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        dots = [Dot3D(point=ax.coords_to_point(1, 1, 0.01), color=RED),
                Dot3D(point=ax.coords_to_point(1, 2, 0.08), color=RED),
                Dot3D(point=ax.coords_to_point(1, 3, 0.03), color=RED),
                Dot3D(point=ax.coords_to_point(1, 4, 0.07), color=RED),

                Dot3D(point=ax.coords_to_point(2, 1, 0.02), color=RED),
                Dot3D(point=ax.coords_to_point(2, 2, 0.05), color=RED),
                Dot3D(point=ax.coords_to_point(2, 3, 0.05), color=RED),
                Dot3D(point=ax.coords_to_point(2, 4, 0.04), color=RED),

                Dot3D(point=ax.coords_to_point(3, 1, 0.04), color=RED),
                Dot3D(point=ax.coords_to_point(3, 2, 0.03), color=RED),
                Dot3D(point=ax.coords_to_point(3, 3, 0.03), color=RED),
                Dot3D(point=ax.coords_to_point(3, 4, 0.06), color=RED),

                Dot3D(point=ax.coords_to_point(4, 1, 0.05), color=RED),
                Dot3D(point=ax.coords_to_point(4, 2, 0.05), color=RED),
                Dot3D(point=ax.coords_to_point(4, 3, 0.10), color=RED),
                Dot3D(point=ax.coords_to_point(4, 4, 0.01), color=RED),

                Dot3D(point=ax.coords_to_point(5, 1, 0.03), color=RED),
                Dot3D(point=ax.coords_to_point(5, 2, 0.08), color=RED),
                Dot3D(point=ax.coords_to_point(5, 3, 0.09), color=RED),
                Dot3D(point=ax.coords_to_point(5, 4, 0.08), color=RED) ]

        self.set_camera_orientation(phi=0, theta=0)
        self.play(ax)
        for i in dots:
            self.play(Create(i))

        self.set_camera_orientation(phi=PI, theta=0)


