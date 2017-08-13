# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def show_mesh(D=None,mesh=None,shownodes=None,showlines=None,shownodelabels=None,showedgelabels=None,showfacelabels=None,showcelllabels=None,pointcolor=None,pointdim=None,linecolor=None,linedim=None,nodelabelcolor=None,edgelabelcolor=None,facelabelcolor=None,celllabelcolor=None,labelsize=None,titlestring=None,xstring=None,ystring=None,zstring=None,xfigsize=None,yfigsize=None,xaxismin=None,xaxismax=None,yaxismin=None,yaxismax=None,zaxismin=None,zaxismax=None,*args,**kwargs):
    varargin = show_mesh.varargin
    nargin = show_mesh.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#   Creation date: March 31st, 2014
#     Last update: June 12th, 2014
    
    #    Description: 
#          Input: 
#         Output: 
#          Notes: get(0,'ScreenSize') to get screen size
##
    
    if 2 == D:
        if 1 == mesh.D:
            f=figure('Position',cat(1,1,xfigsize,yfigsize))
            if shownodes:
                for i in arange(1,mesh.totN).reshape(-1):
                    plot(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),strcat(cat(pointcolor,'.')),'LineWidth',pointdim)
                    hold('on')
            if showlines:
                for l in arange(1,mesh.Nlinesdim1).reshape(-1):
                    plot(mesh.coordlines.dim1free(l,1),mesh.coordlines.dim1free(l,2),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                    hold('on')
            if shownodelabels:
                for i in arange(1,mesh.totN).reshape(-1):
                    text(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),num2str(mesh.nodes.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',nodelabelcolor)
                    hold('on')
            if showedgelabels:
                for i in arange(1,mesh.totE).reshape(-1):
                    text(mesh.edges.centroid(1,i),mesh.edges.centroid(2,i),num2str(mesh.edges.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',edgelabelcolor)
                    hold('on')
            grid('on')
            axis(cat(xaxismin,xaxismax,yaxismin,yaxismax))
            axis('equal')
            xlabel(xstring)
            ylabel(ystring)
            title(titlestring)
        else:
            if 2 == mesh.D:
                f=figure('Position',cat(1,1,xfigsize,yfigsize))
                if shownodes:
                    for i in arange(1,mesh.totN).reshape(-1):
                        plot(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),strcat(cat(pointcolor,'.')),'LineWidth',pointdim)
                        hold('on')
                if showlines:
                    for j in arange(1,mesh.Ndim2).reshape(-1):
                        for l in arange(1,mesh.Nlinesdim1).reshape(-1):
                            plot(mesh.coordlines.dim1free(l,dot(3,(j - 1)) + 1),mesh.coordlines.dim1free(l,dot(3,(j - 1)) + 2),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                            hold('on')
                    for k in arange(1,mesh.Ndim1).reshape(-1):
                        for l in arange(1,mesh.Nlinesdim2).reshape(-1):
                            plot(mesh.coordlines.dim2free(l,dot(3,(k - 1)) + 1),mesh.coordlines.dim2free(l,dot(3,(k - 1)) + 2),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                            hold('on')
                if shownodelabels:
                    for i in arange(1,mesh.totN).reshape(-1):
                        text(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),num2str(mesh.nodes.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',nodelabelcolor)
                        hold('on')
                if showedgelabels:
                    for i in arange(1,mesh.totE).reshape(-1):
                        text(mesh.edges.centroid(1,i),mesh.edges.centroid(2,i),num2str(mesh.edges.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',edgelabelcolor)
                        hold('on')
                if showfacelabels:
                    for i in arange(1,mesh.totF).reshape(-1):
                        text(mesh.faces.centroid(1,i),mesh.faces.centroid(2,i),num2str(mesh.faces.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',facelabelcolor)
                        hold('on')
                grid('on')
                axis(cat(xaxismin,xaxismax,yaxismin,yaxismax))
                axis('equal')
                xlabel(xstring)
                ylabel(ystring)
                title(titlestring)
            else:
                if 3 == mesh.D:
                    disp('Dimensions do not match')
                    f=0
    else:
        if 3 == D:
            if 1 == mesh.D:
                f=figure('Position',cat(1,1,xfigsize,yfigsize))
                if shownodes:
                    for i in arange(1,mesh.totN).reshape(-1):
                        plot3(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),strcat(cat(pointcolor,'.')),'LineWidth',pointdim)
                        hold('on')
                if showlines:
                    for l in arange(1,mesh.Nlinesdim1).reshape(-1):
                        plot3(mesh.coordlines.dim1free(l,1),mesh.coordlines.dim1free(l,2),mesh.coordlines.dim1free(l,3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                        hold('on')
                if shownodelabels:
                    for i in arange(1,mesh.totN).reshape(-1):
                        text(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),num2str(mesh.nodes.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',nodelabelcolor)
                        hold('on')
                if showedgelabels:
                    for i in arange(1,mesh.totE).reshape(-1):
                        text(mesh.edges.centroid(1,i),mesh.edges.centroid(2,i),mesh.edges.centroid(3,i),num2str(mesh.edges.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',edgelabelcolor)
                        hold('on')
                grid('on')
                axis(cat(xaxismin,xaxismax,yaxismin,yaxismax,zaxismin,zaxismax))
                axis('equal')
                xlabel(xstring)
                ylabel(ystring)
                zlabel(zstring)
                title(titlestring)
            else:
                if 2 == mesh.D:
                    f=figure('Position',cat(1,1,xfigsize,yfigsize))
                    if shownodes:
                        for i in arange(1,mesh.totN).reshape(-1):
                            plot3(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),strcat(cat(pointcolor,'.')),'LineWidth',pointdim)
                            hold('on')
                    if showlines:
                        for j in arange(1,mesh.Ndim2).reshape(-1):
                            for l in arange(1,mesh.Nlinesdim1).reshape(-1):
                                plot3(mesh.coordlines.dim1free(l,dot(3,(j - 1)) + 1),mesh.coordlines.dim1free(l,dot(3,(j - 1)) + 2),mesh.coordlines.dim1free(l,dot(3,(j - 1)) + 3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                                hold('on')
                        for k in arange(1,mesh.Ndim1).reshape(-1):
                            for l in arange(1,mesh.Nlinesdim2).reshape(-1):
                                plot3(mesh.coordlines.dim2free(l,dot(3,(k - 1)) + 1),mesh.coordlines.dim2free(l,dot(3,(k - 1)) + 2),mesh.coordlines.dim2free(l,dot(3,(k - 1)) + 3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                                hold('on')
                    if shownodelabels:
                        for i in arange(1,mesh.totN).reshape(-1):
                            text(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),num2str(mesh.nodes.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',nodelabelcolor)
                            hold('on')
                    if showedgelabels:
                        for i in arange(1,mesh.totE).reshape(-1):
                            text(mesh.edges.centroid(1,i),mesh.edges.centroid(2,i),mesh.edges.centroid(3,i),num2str(mesh.edges.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',edgelabelcolor)
                            hold('on')
                    if showfacelabels:
                        for i in arange(1,mesh.totF).reshape(-1):
                            text(mesh.faces.centroid(1,i),mesh.faces.centroid(2,i),mesh.faces.centroid(3,i),num2str(mesh.faces.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',facelabelcolor)
                            hold('on')
                    grid('on')
                    axis(cat(xaxismin,xaxismax,yaxismin,yaxismax,zaxismin,zaxismax))
                    axis('equal')
                    xlabel(xstring)
                    ylabel(ystring)
                    zlabel(zstring)
                    title(titlestring)
                else:
                    if 3 == mesh.D:
                        f=figure('Position',cat(1,1,xfigsize,yfigsize))
                        if shownodes:
                            for i in arange(1,mesh.totN).reshape(-1):
                                plot3(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),strcat(cat(pointcolor,'.')),'LineWidth',pointdim)
                                hold('on')
                        if showlines:
                            for i in arange(1,mesh.Ndim3).reshape(-1):
                                for j in arange(1,mesh.Ndim2).reshape(-1):
                                    for l in arange(1,mesh.Nlinesdim1).reshape(-1):
                                        plot3(mesh.coordlines.dim1free(l,dot(3,(j - 1)) + dot(dot(3,mesh.Ndim2),(i - 1)) + 1),mesh.coordlines.dim1free(l,dot(3,(j - 1)) + dot(dot(3,mesh.Ndim2),(i - 1)) + 2),mesh.coordlines.dim1free(l,dot(3,(j - 1)) + dot(dot(3,mesh.Ndim2),(i - 1)) + 3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                                        hold('on')
                            for i in arange(1,mesh.Ndim3).reshape(-1):
                                for k in arange(1,mesh.Ndim1).reshape(-1):
                                    for l in arange(1,mesh.Nlinesdim2).reshape(-1):
                                        plot3(mesh.coordlines.dim2free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(i - 1)) + 1),mesh.coordlines.dim2free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(i - 1)) + 2),mesh.coordlines.dim2free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(i - 1)) + 3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                                        hold('on')
                            for j in arange(1,mesh.Ndim2).reshape(-1):
                                for k in arange(1,mesh.Ndim1).reshape(-1):
                                    for l in arange(1,mesh.Nlinesdim3).reshape(-1):
                                        plot3(mesh.coordlines.dim3free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(j - 1)) + 1),mesh.coordlines.dim3free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(j - 1)) + 2),mesh.coordlines.dim3free(l,dot(3,(k - 1)) + dot(dot(3,mesh.Ndim1),(j - 1)) + 3),strcat(cat(linecolor,'-')),'LineWidth',linedim)
                                        hold('on')
                        if shownodelabels:
                            for i in arange(1,mesh.totN).reshape(-1):
                                text(mesh.nodes.meshcoordinates(1,i),mesh.nodes.meshcoordinates(2,i),mesh.nodes.meshcoordinates(3,i),num2str(mesh.nodes.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',nodelabelcolor)
                                hold('on')
                        if showedgelabels:
                            for i in arange(1,mesh.totE).reshape(-1):
                                text(mesh.edges.centroid(1,i),mesh.edges.centroid(2,i),mesh.edges.centroid(3,i),num2str(mesh.edges.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',edgelabelcolor)
                                hold('on')
                        if showfacelabels:
                            for i in arange(1,mesh.totF).reshape(-1):
                                text(mesh.faces.centroid(1,i),mesh.faces.centroid(2,i),mesh.faces.centroid(3,i),num2str(mesh.faces.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',facelabelcolor)
                                hold('on')
                        if showcelllabels:
                            for i in arange(1,mesh.totC).reshape(-1):
                                text(mesh.cells.centroid(1,i),mesh.cells.centroid(2,i),mesh.cells.centroid(3,i),num2str(mesh.cells.id(i)),'VerticalAlignment','middle','HorizontalAlignment','left','FontSize',labelsize,'Color',celllabelcolor)
                                hold('on')
                        grid('on')
                        axis(cat(xaxismin,xaxismax,yaxismin,yaxismax,zaxismin,zaxismax))
                        axis('equal')
                        xlabel(xstring)
                        ylabel(ystring)
                        zlabel(zstring)
                        title(titlestring)
    
    return f