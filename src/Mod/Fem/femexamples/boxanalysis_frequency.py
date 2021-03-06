# ***************************************************************************
# *   Copyright (c) 2019 Bernd Hahnebach <bernd@bimstatik.org>              *
# *   Copyright (c) 2020 Sudhanshu Dubey <sudhanshu.thethunder@gmail.com    *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

# to run the example use:
"""
from femexamples.boxanalysis_frequency import setup
setup()

"""

import ObjectsFem

from .boxanalysis_base import setup_boxanalysisbase


def get_information():
    return {
        "name": "Box Analysis Frequency",
        "meshtype": "solid",
        "meshelement": "Tet10",
        "constraints": [],
        "solvers": ["calculix"],
        "material": "solid",
        "equation": "frequency"
    }


def setup(doc=None, solvertype="ccxtools"):

    # setup box frequency, change solver attributes
    doc = setup_boxanalysisbase(doc, solvertype)
    analysis = doc.Analysis

    # solver
    if solvertype == "calculix":
        solver_obj = ObjectsFem.makeSolverCalculix(doc, "SolverCalculiX")
    elif solvertype == "ccxtools":
        solver_obj = ObjectsFem.makeSolverCalculixCcxTools(doc, "CalculiXccxTools")
        solver_obj.WorkingDir = u""
    if solvertype == "calculix" or solvertype == "ccxtools":
        solver_obj.AnalysisType = "frequency"
        solver_obj.GeometricalNonlinearity = "linear"
        solver_obj.ThermoMechSteadyState = False
        solver_obj.MatrixSolverType = "default"
        solver_obj.IterationsControlParameterTimeUse = False
        solver_obj.EigenmodesCount = 10
        solver_obj.EigenmodeHighLimit = 1000000.0
        solver_obj.EigenmodeLowLimit = 0.01
    analysis.addObject(solver_obj)

    doc.recompute()
    return doc
