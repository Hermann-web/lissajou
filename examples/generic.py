import sys

import numpy as np
from matplotlib import pyplot as plt

sys.path.append(".")

from lissajou.anim import (
    BaseAnimation,
    ImageAnimation,
    ParametricAnimation,
    ThreeDimensionalParametricAnimation,
)


class CustomImageAnimation(BaseAnimation):
    """
    A subclass of BaseAnimation for creating animations with custom image data.

    This class generates a random binary image and updates the animation view with the computed sine values for each frame.
    """

    def __init__(self, n):
        """
        Initializes the CustomImageAnimation object.

        Args:
            n (int): The size of the square image (n x n).
        """
        super().__init__()  # Call the superclass constructor to set up the animation
        self.n = n
        self.x = np.random.binomial(1, 0.3, size=(n, n))  # Generate random binary image

    def _set_params(self, **kwargs):
        """
        Sets the parameters for the animation.

        Overrides the base class method but does not add any additional parameters.

        Args:
            **kwargs: Additional keyword arguments for animation parameters.
        """
        super()._set_params(
            **kwargs
        )  # Call the superclass method to handle any common parameters

    def __set_axes__(self):
        """
        Sets up the figure and axes for the animation.

        Returns:
            A tuple (fig, ax) with the matplotlib figure and axes objects.
        """
        fig, ax = plt.subplots()
        return fig, ax

    def _before_each_iteration(self, t):
        """
        Hook method called before each frame iteration.

        This method is overridden but not used in this subclass.

        Args:
            t (int): The current frame number.
        """
        pass  # No pre-iteration setup is needed for this subclass

    def __initialize_view_data__(self, t, ax):
        """
        Initializes the view data for the animation with the initial image.

        Args:
            t (int): The current frame number (not used in this method).
            ax (matplotlib.axes.Axes): The axes object for the animation.

        Returns:
            The initial view data for the animation, represented as an image.
        """
        view = ax.imshow(
            self.x, cmap=plt.cm.gray
        )  # Display the initial image on the axes
        return view

    def __reset_view_data__(self, t, view):
        """
        Updates the view data for each frame of the animation with computed image values.

        Args:
            t (int): The current frame number.
            view: The view data from the previous frame (image object).

        Returns:
            The updated view data for the current frame.
        """
        _ = self.fim(t)  # Compute image values for the current frame
        view.set_array(_)  # Update the image array
        return view

    def fim(self, t):
        """
        Computes the image values for each frame using a custom function.

        Args:
            t (int): The current frame number.

        Returns:
            Computed image values as a NumPy array.
        """
        return np.sin(t * self.x)  # Compute sine values for the current frame


class SinusoidalImageAnimation(ImageAnimation):
    """
    A subclass of ImageAnimation for creating animations with sinusoidal image data.

    This class generates sinusoidal image data and updates the animation view with
    the computed sine values for each frame.
    """

    def __init__(self, n):
        """
        Initializes the SinusoidalImageAnimation object with sinusoidal image data.

        Args:
            n (int): The size of the square image (n x n).
        """
        self.x = np.random.binomial(1, 0.3, size=(n, n))  # Generate random binary image
        super().__init__()  # Call the superclass constructor to set up the animation

    def _set_params(self, **kwargs):
        """
        Sets the parameters for the animation, including the shape of the image.

        Overrides the base class method to ensure the shape parameter matches the
        shape of the generated image.

        Args:
            **kwargs: Additional keyword arguments for animation parameters.

        Returns:
            The result of the superclass method call.
        """
        kwargs["shape"] = (
            self.x.shape
        )  # Set the shape parameter based on the generated image
        return super()._set_params(
            **kwargs
        )  # Call the superclass method to set parameters

    def _before_each_iteration(self, t):
        """
        Hook method called before each frame iteration.

        This method is overridden but not used in this subclass.

        Args:
            t (int): The current frame number.
        """
        pass  # No pre-iteration setup is needed for this subclass

    def _img_fct(self, t):
        """
        Computes the image values for each frame using sine function.

        Overrides the base class method to generate sinusoidal image data.

        Args:
            t (int): The current frame number.

        Returns:
            Computed image values as a NumPy array.
        """
        return np.sin(t * self.x)  # Compute sine values for the current frame


class SinusoidalParametricAnimation(ParametricAnimation):
    """
    A subclass of ParametricAnimation for creating sinusoidal parametric animations.

    This class generates parametric data for x and y coordinates using sinusoidal functions.
    """

    def __init__(self, n):
        """
        Initializes the SinusoidalParametricAnimation object.

        Args:
            n (int): The number of points to generate along the x-axis.
        """
        self.n = n
        super().__init__()  # Call the superclass constructor to set up the animation

    def _before_each_iteration(self, t):
        """
        Hook method called before each frame iteration.

        This method is overridden but not used in this subclass.

        Args:
            t (int): The current frame number.
        """
        pass  # No pre-iteration setup is needed for this subclass

    def _fx(self, t):
        """
        Computes the x-coordinate values for each frame using a linear space.

        Args:
            t (int): The current frame number.

        Returns:
            Computed x-coordinate values as a NumPy array.
        """
        return np.linspace(0, 2 * np.pi, self.n)  # Generate linearly spaced x values

    def _fy(self, t):
        """
        Computes the y-coordinate values for each frame using a sine function.

        Args:
            t (int): The current frame number.

        Returns:
            Computed y-coordinate values as a NumPy array.
        """
        return np.sin(t * self._fx(t))  # Generate y values based on the sine of x


class ThreeDsinusoidalParametricAnimation(ThreeDimensionalParametricAnimation):
    """
    A subclass of ThreeDimensionalParametricAnimation for creating 3D sinusoidal parametric animations.

    This class generates parametric data for x, y, and z coordinates using sinusoidal functions.
    """

    def __init__(self, n):
        """
        Initializes the ThreeDsinusoidalParametricAnimation object.

        Args:
            n (int): The number of points to generate along the x-axis.
        """
        self.n = n
        super().__init__()  # Call the superclass constructor to set up the animation

    def _before_each_iteration(self, t):
        """
        Hook method called before each frame iteration.

        This method is overridden to generate new x-values for each frame.

        Args:
            t (int): The current frame number.
        """
        self.tx = np.linspace(-np.pi, np.pi, self.n)  # Generate x values for each frame

    def _fx(self, t):
        """
        Computes the x-coordinate values for each frame using a sinusoidal function.

        Args:
            t (int): The current frame number.

        Returns:
            Computed x-coordinate values as a NumPy array.
        """
        return np.sin(t * self.tx)  # Generate x values based on the sine of tx

    def _fy(self, t):
        """
        Computes the y-coordinate values for each frame using a sinusoidal function.

        Args:
            t (int): The current frame number.

        Returns:
            Computed y-coordinate values as a NumPy array.
        """
        return np.cos(t * self.tx)  # Generate y values based on the cosine of tx

    def _fz(self, t):
        """
        Computes the z-coordinate values for each frame using a hyperbolic tangent function.
        """
        return np.tanh(
            t * self.tx
        )  # Generate z values based on the hyperbolic tangent of tx


if __name__ == "__main__":

    print("Example 1/4: CustomImageAnimation")
    liss = CustomImageAnimation(10)
    liss.show()

    print("Example 2/4: SinusoidalImageAnimation")
    liss = SinusoidalImageAnimation(100)
    liss.show()

    print("Example 3/4: SinusoidalParametricAnimation")
    liss = SinusoidalParametricAnimation(100)
    liss.show(x_range=(0, 1), y_range=(-1, 1))

    print("Example 4/4: ThreeDsinusoidalParametricAnimation")
    liss = ThreeDsinusoidalParametricAnimation(100)
    liss.show(x_range=(-1, 1), y_range=(-1, 1), z_range=(-1, 1))
