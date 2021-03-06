# Copyright 2020 Intelligent Robotics Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

  stdout_linebuf_envvar = SetEnvironmentVariable(
    'RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED', '1')

  second_launcher_cmd = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(os.path.join(
      get_package_share_directory('launchers_ros2'),
        'launch',
        'second_launch.py')),
    launch_arguments={'message': "Dear student, nice to meet you"}.items())

  #second_launcher_cmd = IncludeLaunchDescription(
  #  PythonLaunchDescriptionSource(os.path.join(
  #    get_package_share_directory('launchers_ros2'),
  #      'launch',
  #      'second_bis_launch.py')))

  ld = LaunchDescription()
  ld.add_action(stdout_linebuf_envvar)
  ld.add_action(second_launcher_cmd)

  return ld
