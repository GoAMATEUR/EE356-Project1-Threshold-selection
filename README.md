# EE356: Project 1
SJTU EE356 Project 1: Threshold selection by clustering gray levels of boundary.

Author: HUANG Siyuan (519030910095)

## Paper Outline

#### 1. Boundary points

All boundary points satisfies:

1. $\frac{\partial^{2}f}{\partial x^{2}} + \frac{\partial^{2}f}{\partial y^{2}}=0$
2. $\sqrt{{\frac{\partial{f}}{\partial{x}}}^2+{\frac{\partial{f}}{\partial{y}}}^2}\ge T$

Where $T$ is predefined.

#### 2. Discrete sampling of gray values of boundaries

Goal: obtain the discrete sampling points of the boundaries within 2D image and the gray values of these discrete sampling points.

2D image is treated as discrete sampling data sampled from the grid points (i.e. pixels lies on the grid points) of 2D regular grids. Two kinds of cells: edge-cells intersected by boundary, non-edge-cells. 

Procedure of finding edge cells:

1. detect all edge-cells
2. approximate the boundary in each edge-cell by examining the number  of interacted edges.

The vertices of a intersected boundary, $$p_1$$ and $$p_2$$ has the following properties:

​	1. $l(p_1) l(p_2) < 0$

​	2. $g(p_1) g(p_2) \ge 2\tilde{T}$

Where gradient threshold $\tilde{T}$ needs to be predefined. The intersected edges can be found in this way. 

The simplest method to compute the position and the gray value of an intersecting point is to linearly interpolate the positions and the gray values of two vertices of the edge at which this intersecting point locates.

In practice, if there exists a boundary between two vertices, we assume its gray value to be the average gray value of the two vertices.

#### 3. Threshold selection method

##### 3.1. Bi-level threshold selection

In the case of 2D image containing only one object class and one background class, the unique cluster exists in the histogram of discrete sampling points of the boundary. Thus, threshold can be selected as the average value of gray values of the discrete sampling points of the boundary.

##### 3.2. Bi-level threshold selection

If there is much noise or other small objects in 2D image, it is better to select threshold at the main peak of histogram of all discrete sampling points. Example: ```1_gray.bmp```.

##### 3.3. Multilevel threshold selection

For 2D image containing more than one interesting object class, multilevel thresholds are needed to select. The means of the clusters in the histogram of gray values of boundary points correspond to thresholds of different segments in the image, exclusive of the background.

## Results

To be uploaded.









