# This file is part of GxPowerIndicator.
# Copyright (C) 2014 Christopher Kyle Horton <christhehorton@gmail.com>

# GxPowerIndicator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GxPowerIndicator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GxPowerIndicator. If not, see <http://www.gnu.org/licenses/>.


# GxPowerIndicator
# This indicator shuts down the SubOS when clicked.

self.SetIcon(pygame.image.load("indicators/default/GxPowerIndicator/shutdown.png")

self.click_code = """
pygame.quit()
sys.exit()
"""

self.frame_code = """
self.image = self.icon
"""
