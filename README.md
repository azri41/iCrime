# PROJECT OVERVIEW

## A. DEFINING THE PROJECT

:fire: **Project Summary**

**Customer:** Polis Diraja Malaysia (PDRM) (Mock)

**Project name:** iCrime

**Team Members:**

- Muhammad Azri Bin Azmi
- Aiman Iskandar Bin Mohd Zaidi
- Ariff Rahimin Bin Mohamed Norazman
- Muhammad Haziq Izzuddin Bin Mohd Junaidy

:grin: **Objectives:**

- Identify criminals by using face recognition.
- Reduce workload for police.
- Improve law enforcement.

## B. PLANNING THE PROJECT

:computer: **Project Management Life-Cycle**

<!-- - [insert Work Breakdown Structure (WBS) for each of the given tasks with Gantt Chart (Screen capture & attached source file, excel or MS Project) for Scope and Plan Project Management. The Gantt Chart includes activities, milestones, summary tasks, Durations of tasks and, etc] -->

![Gantt Chart](https://github.com/azri41/iCrime/blob/main/images/gantt_chart.PNG)

<div  align="center"><em>Figure 1: Gantt Chart</em></div>
<br><br>

![Work Breakdown Structure](https://github.com/azri41/iCrime/blob/main/images/WBS.PNG)

<div align="center"><em>Figure 2: Work Breakdown Structure</em></div>

<br><br>
:chart: **Risk Identification Chart** (Quality, Cost, Time)

| Control Element | What is likely to go wrong?                   | How and when will I know?                                  | What will I do about it?                                                               |
| --------------- | --------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Quality         | Faces could not detect accurately.            | Cameras detect wrong criminals faces.                      | Modify the algorithm like threshold to detect the faces.                               |
| Cost            | Overexpensive equipments such as cameras.     | Funds are spend to hardware only.                          | Find new suppliers to cover the costs.                                                 |
| Time            | Time consuming to collect and train the data. | Training process took so long and sometimes have an error. | Train the data by using GPU instead of CPU or using cloud computing like Google Colab. |

:green_book: **Responsibility Assignment Matrices (RAM) :**

![Responsibility Assignment Matrices (RAM)](https://github.com/azri41/iCrime/blob/main/images/RAM.PNG)

<div align="center"><em>Figure 3: Responsibility Assignment Matrices</em></div><br>

| Name                                     | Roles                   |
| ---------------------------------------- | ----------------------- |
| Muhammad Azri Bin Azmi                   | Project Manager         |
| Aiman Iskandar Bin Mohd Zaidi            | Design Technician       |
| Ariff Rahimin Bin Mohamed Norazman       | Lead Engineer           |
| Muhammad Haziq Izzuddin Bin Mohd Junaidy | Senior Project Director |

<br>

:pushpin: **Project Planning Summary:**

| Modules/Components        | Budget (RM)  | Schedule                          | Responsibility           |
| ------------------------- | ------------ | --------------------------------- | ------------------------ |
| Criminal Database         | 500,000.00   | 30 December 2020 - 9 January 2021 | Collect Data, Label Data |
| Criminal Face Recognition | 1,200,000.00 | 17 January 2021 - 30 January 2021 | Train model, Test model  |
| Map Tracking              | 120,000.00   | 10 January 2021 - 16 January 2021 | Connect system with GPS  |

## C. IMPLEMENTING THE PROJECT PLAN

:mailbox_with_mail: **Deliverables:**

- Planning Deliverables
- Analysis Deliverables
- Design Deliverables
- Implementation Deliverables

:open_file_folder: **Tasks and Estimated Costs**

| Task        | Estimated Costs(RM) | Notes                                                 |
| ----------- | ------------------- | ----------------------------------------------------- |
| Acquisition | 5,272,630.00        | -                                                     |
| Design      | 391,110.00          | System Design, Data Collection                        |
| Restoration | 1,328,972.00        | Camera Installation, System Installation, Maintenance |

<br>

:calendar: **Milestone Chart**

| Milestone      | Scheduled Completion | Actual Completion |
| -------------- | -------------------- | ----------------- |
| Planning       | 28 November 2020     | 27 November 2020  |
| Analysis       | 30 December 2020     | 21 December 2020  |
| Design         | 29 January 2021      | 30 January 2021   |
| Implementation | 28 February 2021     | 26 February 2021  |

<br>

## D. EXECUTING THE PROJECT

:bulb: **Project Design and coding**

**Flow Diagram**

![Flow](https://github.com/azri41/iCrime/blob/main/images/design.png)

<div align="center"><em>Figure 4: Flow Diagram</em></div><br>

:grin: **CODING:**

**Face Recognition**
<br>
Command: <em>pip install -r requirement.txt</em>

- Use this command to install the required packages.
<br>
<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Bounding%20Box.JPG"></div>
<div align="center"><strong><em>Figure 5: Bounding Box</em></strong></div>
For every face that are detected, a box will be placed based on the face locations. It will crop the face, and apply the model that we train, to recognize the face.<br><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Filter_Algo.JPG"></div>
<div align="center"><strong><em>Figure 6: Filter algorithm</em></strong></div>
This algorithm filters raw images and select images that have face, and remove images that have no face or bad to detect face.<br><br>
<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Training_Model.JPG"></div>
<div align="center"><strong><em>Figure 7: Training model</em></strong></div>
Images with each label(their folder), are being extracted and trained with MTCNN. <br><br>

**PATH PLANNING**

- After camera can recognize the criminal face, this algorithm will execute to search the shortest path from police station to criminal(camera)
- In this project, we use Breadth First Search algorithm for path searching

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/main.PNG"></div>
<div align="center"><strong><em>Figure 9: Main Coding For Path Searching</em></strong></div>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/maze.PNG"></div>
<div align="center"><strong><em>Figure 10: Map</em></strong></div>
 The map is hard coding in python. This is the example of maze that have 9x9 dimension.<br><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/findend.PNG"></div>
<div align="center"><strong><em>Figure 11: Path Planning Algorithm: Breadth First Search</em></strong></div>
 It will find the shortest path between the starting point and any other reachable node.<br><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/result.PNG"></div>
<div align="center"><strong><em>Figure 12: Path Planning Result</em></strong></div>
 The red color plus symbol shows the path to criminal and white hash symbol shows the building<br><br>

:stars: **Project Result**

- Our results contain of labeled face with its confidence level. Figure below shows our system results:

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Aiman_Capture.JPG"></div>
<div align="center"><em>Figure 13: Aiman face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Ariff_Capture.JPG"></div>
<div align="center"><em>Figure 14: Ariff face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Azri_Capture.JPG"></div>
<div align="center"><em>Figure 15: Azri face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Izz_Capture.JPG"></div>
<div align="center"><em>Figure 16: Haziq face result</em></div><br>

## E. COMPLETING THE PROJECT

:clipboard: **Closing Checklist**
<br>
:heavy_check_mark: [Sign Off](https://github.com/azri41/iCrime/blob/main/images/SignOff.PNG)
<br>
:heavy_check_mark: [Lesson Learned](https://github.com/azri41/iCrime/blob/main/Project%20Documentation/12%20Project%20Closing.pdf)
<br>
:heavy_check_mark: [Final Project Report](https://github.com/azri41/iCrime/blob/main/README.md)
<br>
:heavy_check_mark: [Close Contract](https://github.com/azri41/iCrime/blob/main/Project%20Documentation/09%20Procurement%20Management%20Plan.pdf)
<br>

## F. PROJECT PRESENTATION

:movie_camera: **Presentation Video**

- Click here to watch our presentation! :wink:

[![iCrime](https://github.com/azri41/iCrime/blob/main/images/thumbnail.JPG)](https://youtu.be/FhC62sJebs8 "iCrime Project Presentation")

<br>

:movie_camera: **System Demonstration Video**

- Click here to watch our system demonstration! :bomb:

[![iCrime](https://github.com/azri41/iCrime/blob/main/images/demo.PNG)](https://youtu.be/oEbJ9gSC598 "iCrime System Demonstration")

:book: **License**
<br>
This project is protected by this [LICENSE](LICENSE.md) :heart:
