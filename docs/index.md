# Table of Contents

* [anim](#anim)
  * [BaseAnimation](#anim.BaseAnimation)
    * [max\_frames](#anim.BaseAnimation.max_frames)
    * [speed](#anim.BaseAnimation.speed)
    * [\_\_init\_\_](#anim.BaseAnimation.__init__)
    * [show](#anim.BaseAnimation.show)
    * [\_\_setup\_\_](#anim.BaseAnimation.__setup__)
    * [\_\_set\_axes\_\_](#anim.BaseAnimation.__set_axes__)
    * [\_\_animate\_\_](#anim.BaseAnimation.__animate__)
    * [\_\_is\_first\_it\_\_](#anim.BaseAnimation.__is_first_it__)
    * [\_\_initialize\_view\_data\_\_](#anim.BaseAnimation.__initialize_view_data__)
    * [\_\_reset\_view\_data\_\_](#anim.BaseAnimation.__reset_view_data__)
  * [ImageAnimation](#anim.ImageAnimation)
    * [width](#anim.ImageAnimation.width)
    * [height](#anim.ImageAnimation.height)
    * [\_\_set\_axes\_\_](#anim.ImageAnimation.__set_axes__)
    * [\_\_initialize\_view\_data\_\_](#anim.ImageAnimation.__initialize_view_data__)
    * [\_\_reset\_view\_data\_\_](#anim.ImageAnimation.__reset_view_data__)
    * [\_\_get\_img\_vals\_\_](#anim.ImageAnimation.__get_img_vals__)
  * [ParametricAnimation](#anim.ParametricAnimation)
    * [x\_range](#anim.ParametricAnimation.x_range)
    * [y\_range](#anim.ParametricAnimation.y_range)
    * [\_\_set\_axes\_\_](#anim.ParametricAnimation.__set_axes__)
    * [\_\_initialize\_view\_data\_\_](#anim.ParametricAnimation.__initialize_view_data__)
    * [\_\_reset\_view\_data\_\_](#anim.ParametricAnimation.__reset_view_data__)
  * [ThreeDimensionalParametricAnimation](#anim.ThreeDimensionalParametricAnimation)
    * [z\_range](#anim.ThreeDimensionalParametricAnimation.z_range)
    * [\_\_set\_axes\_\_](#anim.ThreeDimensionalParametricAnimation.__set_axes__)
    * [\_\_initialize\_view\_data\_\_](#anim.ThreeDimensionalParametricAnimation.__initialize_view_data__)
    * [\_\_reset\_view\_data\_\_](#anim.ThreeDimensionalParametricAnimation.__reset_view_data__)
* [lissajou](#lissajou)
  * [GenericLissajou](#lissajou.GenericLissajou)
  * [VaryingAmplitudeLissajou](#lissajou.VaryingAmplitudeLissajou)
  * [SinusoidalAmplitudeLissajou](#lissajou.SinusoidalAmplitudeLissajou)
  * [FixedRatioLissajou](#lissajou.FixedRatioLissajou)
  * [EllipticLissajou](#lissajou.EllipticLissajou)
  * [CircularLissajou](#lissajou.CircularLissajou)

<a id="anim"></a>

# anim

File: animation_framework.py
Author: Hermann Agossou

Description:
    This file contains a framework for creating animations using matplotlib.
    It defines abstract base classes and subclasses for creating various types
    of animations, including parametric animations and 3D parametric animations.

<a id="anim.BaseAnimation"></a>

## BaseAnimation Objects

```python
class BaseAnimation(metaclass=ABCMeta)
```

An abstract base class designed to simplify the creation of animations using matplotlib.

This class defines a framework for creating animations by specifying setup steps,
frame updates, and parameters. Subclasses should provide implementations for abstract
methods to define specific animation behaviors.

<a id="anim.BaseAnimation.max_frames"></a>

#### max\_frames

Default maximum number of frames

<a id="anim.BaseAnimation.speed"></a>

#### speed

Default frame interval in milliseconds (33.33ms for 30 FPS)

<a id="anim.BaseAnimation.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Constructor for the BaseAnimation class.

<a id="anim.BaseAnimation.show"></a>

#### show

```python
def show(**kwargs)
```

Sets up the animation and displays it.

Accepts various keyword arguments to customize animation parameters before display.

<a id="anim.BaseAnimation.__setup__"></a>

#### \_\_setup\_\_

```python
def __setup__(**kwargs)
```

Private method for initial setup of the animation. It configures parameters,
sets up the figure and axes, and initializes the animation.

**Arguments**:

- `**kwargs` - Arbitrary keyword arguments for animation parameters.

<a id="anim.BaseAnimation.__set_axes__"></a>

#### \_\_set\_axes\_\_

```python
@abstractmethod
def __set_axes__()
```

Abstract method for setting up the axes of the figure.

Subclasses must implement this method to define the axes setup.

**Returns**:

  A tuple containing the figure and axes objects.

<a id="anim.BaseAnimation.__animate__"></a>

#### \_\_animate\_\_

```python
def __animate__(t)
```

Private method to update the animation at each frame.

**Arguments**:

- `t` _int_ - The current frame number.
  

**Returns**:

  A tuple containing the elements to update for the current frame.

<a id="anim.BaseAnimation.__is_first_it__"></a>

#### \_\_is\_first\_it\_\_

```python
def __is_first_it__(t)
```

Check if the current frame is the first one.

**Arguments**:

- `t` _int_ - The current frame number.
  

**Returns**:

- `bool` - True if this is the first frame, False otherwise.

<a id="anim.BaseAnimation.__initialize_view_data__"></a>

#### \_\_initialize\_view\_data\_\_

```python
@abstractmethod
def __initialize_view_data__(t, ax)
```

Abstract method to initialize the view data for the first frame of the animation.

**Arguments**:

- `t` _int_ - The current frame number.
- `ax` _matplotlib.axes.Axes_ - The axes object for the animation.
  

**Returns**:

  Initial view data for the animation. This can be matplotlib artists or any data structure
  that represents the initial state of the animated elements.

<a id="anim.BaseAnimation.__reset_view_data__"></a>

#### \_\_reset\_view\_data\_\_

```python
@abstractmethod
def __reset_view_data__(t, view)
```

Abstract method to update the view data for each subsequent frame after the first.

This method should update the state of the animated elements based on the current frame number.

**Arguments**:

- `t` _int_ - The current frame number.
- `view` - The view data from the previous frame, to be updated for the current frame.
  

**Returns**:

  Updated view data for the current frame. This is typically the same object(s) as `view`,
  but updated to reflect the new frame's state.

<a id="anim.ImageAnimation"></a>

## ImageAnimation Objects

```python
class ImageAnimation(BaseAnimation)
```

A subclass of BaseAnimation designed for creating animations with image data.

This class initializes animation view data with random binary images and allows for
updating the view data using a custom image function '_img_fct' for each frame.

<a id="anim.ImageAnimation.width"></a>

#### width

Width of the image

<a id="anim.ImageAnimation.height"></a>

#### height

Height of the image

<a id="anim.ImageAnimation.__set_axes__"></a>

#### \_\_set\_axes\_\_

```python
def __set_axes__()
```

Sets up the figure and axes for the animation.

**Returns**:

  A tuple (fig, ax) with the matplotlib figure and axes objects.

<a id="anim.ImageAnimation.__initialize_view_data__"></a>

#### \_\_initialize\_view\_data\_\_

```python
def __initialize_view_data__(t, ax)
```

Initializes the view data for the animation with random binary images.

**Arguments**:

- `t` _int_ - The current frame number (not used in this method).
- `ax` _matplotlib.axes.Axes_ - The axes object for the animation.
  

**Returns**:

  The initial view data for the animation, represented as an image.

<a id="anim.ImageAnimation.__reset_view_data__"></a>

#### \_\_reset\_view\_data\_\_

```python
def __reset_view_data__(t, view)
```

Updates the view data for each frame of the animation with computed image values.

**Arguments**:

- `t` _int_ - The current frame number.
- `view` - The view data from the previous frame (image object).
  

**Returns**:

  The updated view data for the current frame.

<a id="anim.ImageAnimation.__get_img_vals__"></a>

#### \_\_get\_img\_vals\_\_

```python
def __get_img_vals__(t) -> np.ndarray
```

Computes the image values for the current frame using a custom image function.

**Arguments**:

- `t` _int_ - The current frame number.
  

**Returns**:

  Computed image values as a NumPy array.

<a id="anim.ParametricAnimation"></a>

## ParametricAnimation Objects

```python
class ParametricAnimation(BaseAnimation, metaclass=ABCMeta)
```

A subclass of BaseAnimation designed for creating parametric animations.

This class introduces x and y ranges for the plot and requires the definition
of parametric functions `_fx` and `_fy` to compute the x and y coordinates of
the plot for each frame based on a parameter `t`.

<a id="anim.ParametricAnimation.x_range"></a>

#### x\_range

Optional x-axis range for the plot

<a id="anim.ParametricAnimation.y_range"></a>

#### y\_range

Optional y-axis range for the plot

<a id="anim.ParametricAnimation.__set_axes__"></a>

#### \_\_set\_axes\_\_

```python
def __set_axes__()
```

Sets up the figure and axes for the animation with optional x and y ranges.

**Returns**:

  A tuple (fig, ax) with the matplotlib figure and axes objects.

<a id="anim.ParametricAnimation.__initialize_view_data__"></a>

#### \_\_initialize\_view\_data\_\_

```python
def __initialize_view_data__(t, ax)
```

Initializes the view data for the animation based on the parametric functions.

**Arguments**:

- `t` _int_ - The current frame number.
- `ax` _matplotlib.axes.Axes_ - The axes object for the animation.
  

**Returns**:

  The initial view data for the animation.

<a id="anim.ParametricAnimation.__reset_view_data__"></a>

#### \_\_reset\_view\_data\_\_

```python
def __reset_view_data__(t, view)
```

Updates the view data for each frame.

**Arguments**:

- `t` _int_ - The current frame number.
- `view` - The view data from the previous frame.
  

**Returns**:

  The updated view data for the current frame.

<a id="anim.ThreeDimensionalParametricAnimation"></a>

## ThreeDimensionalParametricAnimation Objects

```python
class ThreeDimensionalParametricAnimation(ParametricAnimation,
                                          metaclass=ABCMeta)
```

A subclass of ParametricAnimation for creating 3D parametric animations.

This class adds a third dimension to the animations, allowing for the creation of
dynamic 3D visualizations. It introduces a z-axis range and requires the definition
of a function `_fz` to compute the z-coordinate for each frame.

<a id="anim.ThreeDimensionalParametricAnimation.z_range"></a>

#### z\_range

Optional z-axis range for the plot

<a id="anim.ThreeDimensionalParametricAnimation.__set_axes__"></a>

#### \_\_set\_axes\_\_

```python
def __set_axes__()
```

Sets up the figure and axes for the 3D animation with optional x, y, and z ranges.

**Returns**:

  A tuple (fig, ax) with the matplotlib figure and 3D axes objects.

<a id="anim.ThreeDimensionalParametricAnimation.__initialize_view_data__"></a>

#### \_\_initialize\_view\_data\_\_

```python
def __initialize_view_data__(t, ax)
```

Initializes the view data for the 3D animation based on the parametric functions.

**Arguments**:

- `t` _int_ - The current frame number.
- `ax` _matplotlib.axes._subplots.Axes3DSubplot_ - The 3D axes object for the animation.
  
  

**Returns**:

  The initial view data for the 3D animation.

<a id="anim.ThreeDimensionalParametricAnimation.__reset_view_data__"></a>

#### \_\_reset\_view\_data\_\_

```python
def __reset_view_data__(t, view)
```

Updates the view data for each frame of the 3D animation.

**Arguments**:

- `t` _int_ - The current frame number.
- `view` - The view data from the previous frame.
  

**Returns**:

  The updated view data for the current frame.

<a id="lissajou"></a>

# lissajou

Lissajous Animation Simulation

This module provides classes for simulating Lissajous curves and generating animations
based on various parameters and configurations.

Classes:
- GenericLissajou: Simulates a generic Lissajous curve animation.
- VaryingAmplitudeLissajou: Simulates a Lissajous curve with varying amplitude.
- SinusoidalAmplitudeLissajou: Simulates a Lissajous curve with a sinusoidal variation in amplitude.
- FixedRatioLissajou: Simulates a Lissajous curve with a fixed ratio of amplitudes.
- EllipticLissajou: Simulates a Lissajous ellipse animation.
- CircularLissajou: Simulates a Lissajous circle animation.

Usage:
Each class provides a method 'show()' to display the animation. Instantiate the desired
class object and call 'show()' to view the animation.

**Example**:

  # Simulate and display a Lissajous ellipse animation
  animation = EllipticLissajou()
  animation.show()

<a id="lissajou.GenericLissajou"></a>

## GenericLissajou Objects

```python
class GenericLissajou(ParametricAnimation)
```

A class for simulating Lissajous curves.

**Arguments**:

- `a` _float_ - The parameter controlling the x-coordinate.
- `b` _float_ - The parameter controlling the y-coordinate.
- `delta` _float_ - The phase difference between the two sine functions.
- `range` _float_ - The range of the parameter 't' for the simulation. A higher range will put more points on each frame
- `nb_points` _int_ - The number of points to generate within the range.
  
  Usage:
    ```python
    # example 1
    animation = GenericLissajou()
    animation.show()
    # exmple2: change lissajou parameters
    animation = GenericLissajou(a=3, b=2, delta=np.pi / 2)
    # example2: change the visualization params
    animation = GenericLissajou(
        a=1, b=2, delta=np.pi / 2, range=50, nb_points=100000
    )
    animation.max_frames = 10000
    animation.show()
    ```

<a id="lissajou.VaryingAmplitudeLissajou"></a>

## VaryingAmplitudeLissajou Objects

```python
class VaryingAmplitudeLissajou(GenericLissajou)
```

A class for simulating Lissajous curves with varying ratios and sinusoidal 'b'.

Usage:
animation = VaryingAmplitudeLissajou()
animation.show()

**Notes**:

  - The parameter 'a' is fixed.
  - The parameter 'delta' is fixed at pi/2.
  - The parameter 'b' follows a sinusoidal function, resulting in dancing curves.

<a id="lissajou.SinusoidalAmplitudeLissajou"></a>

## SinusoidalAmplitudeLissajou Objects

```python
class SinusoidalAmplitudeLissajou(GenericLissajou)
```

A class for simulating Lissajous curves with a constant sinusoidal effect on 'b'.

Usage:
animation = SinusoidalAmplitudeLissajou()
animation.show()

**Notes**:

  - The parameter 'a' is fixed.
  - The parameter 'delta' is fixed at pi/2.
  - The parameter 'b' varies with cosine of time for interesting effects.

<a id="lissajou.FixedRatioLissajou"></a>

## FixedRatioLissajou Objects

```python
class FixedRatioLissajou(GenericLissajou)
```

A class for simulating closed Lissajous curves with fixed ratio 'b/a'.

**Arguments**:

- `a` _float_ - The parameter controlling the x-coordinate.
- `delta` _float_ - The phase difference between the two sine functions.
- `range` _float_ - The range of the parameter 't' for the simulation.
- `nb_points` _int_ - The number of points to generate within the range.
- `ratio` _float_ - The fixed ratio between 'b' and 'a'.
  
  Usage:
  animation = FixedRatioLissajou()
  animation.show()
  

**Notes**:

  - The ratio 'b/a' is kept constant to produce closed curves.

<a id="lissajou.EllipticLissajou"></a>

## EllipticLissajou Objects

```python
class EllipticLissajou(FixedRatioLissajou)
```

A class for simulating Lissajous ellipses.

Usage:
animation = EllipticLissajou()
animation.show()

**Notes**:

  - The ratio 'b/a' is kept constant to produce ellipses.

<a id="lissajou.CircularLissajou"></a>

## CircularLissajou Objects

```python
class CircularLissajou(EllipticLissajou)
```

A class for simulating Lissajous circles.

Usage:
animation = CircularLissajou()
animation.show()

**Notes**:

  - The ratio 'b/a' is kept constant to produce circles.
  - The phase difference 'delta' is set to pi/2 to produce circles.

