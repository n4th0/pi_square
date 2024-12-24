from manim import *



class variations(Scene):
    def construct(self):


        b = VGroup()
        for i in range(-2, 4, 2):
            b.add(Square().scale(1/2).shift(i*RIGHT))


        text2 = MathTex(r"V^n_m = \frac{m!}{(m-n)!}")
        text = MathTex(r"V^3_5 = \frac{5!}{(5-3)!} = 60")
        self.play(Create(text2))
        self.wait(2)
        self.play(ReplacementTransform(text2, text))

        self.wait(3)

        text3 = VGroup(
        Tex("x").shift(-1*RIGHT),
        Tex("x").shift(1*RIGHT),
        Tex("5").shift(-2*RIGHT),
        Tex("4"),
        Tex("3").shift(2*RIGHT),
        b)

        self.remove(text)

        self.play(ReplacementTransform(text, text3))
        # self.wait(3)

        # i have to compute all 60 combinations
        a = [1, 2, 3, 4, 5]
        something = []
        
        def function(arr, total):
            if len(arr) == 3:
                # print(arr)
                something.append(arr)
                return
        
            for i in total:
                if i not in arr:
                    # print(i)
                    b = arr[:]
                    b.append(i)
                    function(b, total)
        
        for i in a:
            arr = [i]
            function(arr, a)

        figure1 = Triangle().scale(1/2).shift(DOWN*0.25).shift(UP*3).shift(LEFT*3).set_stroke(2)
        figure2 = Triangle().rotate(60*DEGREES).scale(1/2).shift(UP*0.15).shift(UP*3).shift(LEFT*1.75).set_stroke(2)
        figure3 = Star(n=8).scale(1/2).shift(UP*3).set_stroke(2)
        figure4 = Circle().scale(1/2).shift(UP*3).shift(RIGHT*1.5).set_stroke(2)
        figure5 = Square().scale(1/2).shift(UP*3).shift(RIGHT*3).set_stroke(2)

        figure1.set_color(ManimColor.from_rgb((255, 190, 11, 1)))
        figure2.set_color(ManimColor.from_rgb((251, 86, 7, 1)))
        figure3.set_color(ManimColor.from_rgb((255, 0, 110, 1)))
        figure4.set_color(ManimColor.from_rgb((131, 56, 236, 1)))
        figure5.set_color(ManimColor.from_rgb((58, 134, 255, 1)))

        self.play(Create(figure1),
        Create(figure2),
        Create(figure3),
        Create(figure4),
        Create(figure5))

        self.wait(1)
        self.play(Uncreate(text3))
        self.wait(1)


        for i in something:
            b = VGroup()
            count = -2

            # I hate the manim shift function
            figure1 = Triangle().scale(1/2).shift(DOWN*0.25)
            figure2 = Triangle().rotate(60*DEGREES).scale(1/2).shift(UP*0.15).shift(LEFT*0.15)
            figure3 = Star(n=8).scale(1/2)
            figure4 = Circle().scale(1/2)
            figure5 = Square().scale(1/2)
            figure1.set_color(ManimColor.from_rgb((255, 190, 11, 1)))
            figure2.set_color(ManimColor.from_rgb((251, 86, 7, 1)))
            figure3.set_color(ManimColor.from_rgb((255, 0, 110, 1)))
            figure4.set_color(ManimColor.from_rgb((131, 56, 236, 1)))
            figure5.set_color(ManimColor.from_rgb((58, 134, 255, 1)))

            for j in i:
                if j == 1:
                    b.add(figure1.shift(count*RIGHT))
                elif j == 2:
                    b.add(figure2.shift(count*RIGHT))
                elif j == 3:
                    b.add(figure3.shift(count*RIGHT))
                elif j == 4:
                    b.add(figure4.shift(count*RIGHT))
                elif j == 5:
                    b.add(figure5.shift(count*RIGHT))
                count +=2

            self.add(b)
            self.wait(0.2)
            self.remove(b)







