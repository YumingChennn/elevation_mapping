import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # elevation_mapping 套件的設定路徑
    share_dir = get_package_share_directory('elevation_mapping')
    config_dir = os.path.join(share_dir, 'config')

    # === elevation_mapping 設定檔 ===
    list_params = []
    for filee in [
        "robots/ground_truth_demo.yaml",
        "elevation_maps/long_range.yaml",
        "sensor_processors/realsense_d435.yaml",
        "postprocessing/postprocessor_pipeline.yaml"
    ]:
        list_params.append(os.path.join(config_dir, filee))

    return LaunchDescription([
        # --- 1️⃣ elevation_mapping 節點 ---
        Node(
            package='elevation_mapping',
            executable='elevation_mapping',
            name='elevation_mapping',
            output='screen',
            parameters=list_params,
        ),

        # --- 2️⃣ robot_state_publisher 節點 ---
        # Node(
        #     package='robot_state_publisher',
        #     executable='robot_state_publisher',
        #     name='robot_state_publisher',
        #     output='screen',
        #     parameters=[{
        #         # 如果是 .xacro 檔案才需要 Command；你的是 .urdf，直接讀取文字內容即可
        #         'robot_description': open(compal_urdf_path).read()
        #     }]
        # )

        # --- 3️⃣ RViz2 顯示 ---
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=[
                '--display-config',
                os.path.join(share_dir, 'rviz2', 'custom_rviz2.rviz')
            ],
            output='screen'
        )
    ])
