# EE356: Project 1
SJTU EE356 Project 1: Threshold selection by clustering gray levels of boundary.

## Paper Outline



#### Discrete sampling of gray values of boundaries

Goal: obtain the discrete sampling points of the boundaries within 2D image and the gray values of these discrete sampling points.

2D image is treated as discrete sampling data sampled from the grid points (i.e. pixels lies on the grid points) of 2D regular grids. Two kinds of cells: edge-cells intersected by boundary, non-edge-cells. 

Procedure of finding edge cells:

1. detect all edge-cells
2. approximate the boundary in each edge-cell by examining the number  of interacted edges.

The vertices of a intersected boundary, p<sub>1</sub> and p<sub>2</sub> has the following properties:

1. $l(p_1) l(p_2) < 0$

2. $g(p_1) g(p_2) > 2\tilde{T}$

Where gradient threshold $\tilde{T}$ needs to be predefined. The intersected edges can be found in this way. 

The simplest method to compute the position and the gray value of an intersecting point is to linearly interpolate the positions and the gray values of two vertices of the edge at which this intersecting point locates.

#### Threshold selection method

##### Bi-level threshold selection











