# PROJECT OVERVIEW

## A. DEFINING THE PROJECT

:fire: **Project Summary**

**Customer:** Polis Diraja Malaysia (PDRM) (Mock)

**Project name:** iCrime

**Team Members:**

- Muhammad Azri Bin Azmi
- Aiman Iskandar Bin Mohd Zaidi
- Ariff Rahimin Bin Mohamed Norazman
- Muhammad Haziq Izzuddin Bin Junaidy

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

- [insert RAM Table include Resource Responsibility, Task/Deliverable (attach a Screen capture of the table).]
- [Insert List for each of the members for their Roles and Responsibilities).]

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
- Maintenance Deliverables

:open_file_folder: **Tasks and Estimated Costs**

| Task        | Estimated Costs(RM) | Notes                                                 |
| ----------- | ------------------- | ----------------------------------------------------- |
| Acquisition | 5,272,630.00        | -                                                     |
| Design      | 391,110.00          | System Design, Data Collection                        |
| Restoration | 1,328,972.00        | Camera Installation, System Installation, Maintenance |

:calendar: **Milestone Chart**

| Milestone      | Scheduled Completion | Actual Completion |
| -------------- | -------------------- | ----------------- |
| Planning       | 28 November 2020     | 27 November 2020  |
| Analysis       | 30 December 2020     | 21 December 2020  |
| Design         | 29 January 2021      | 30 January 2020   |
| Implementation | 28 February 2021     | 26 February 2020  |
| Maintainance   | 29 March 2021        | 1 April 2020      |

## D. EXECUTING THE PROJECT

:bulb: **Project Design and coding**

**Flow Diagram**

![Flow](https://github.com/azri41/iCrime/blob/main/images/design.png)
<div align="center"><em style="color: green;">Figure 3: Flow Diagram</em></div><br>

:grin: **CODING:**

**Face Recognition**
<br>
Command: <em>pip install -r requirement.txt</em>
- Use this command to install the required packages.
<br>
<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Bounding%20Box.JPG"></div>
<div align="center"><em>Figure 4: </em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Filter_Algo.JPG"></div>
<div align="center"><em>Figure 5: </em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Training_Model.JPG"></div>
<div align="center"><em>Figure 6:</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Main%20Detection.PNG"></div>
<div align="center"><em>Figure 7: </em></div><br>

**PATH PLANNING**
- After camera can recognize the criminal face, this algorithm will execute to search the shortest path from police station to criminal(camera)
- In this project, we use Breadth First Search algorithm for path searching

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/main.PNG"></div>
<div align="center"><em>Figure 8: Main Coding For Path Searching</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/maze.PNG"></div>
<div align="center"><em>Figure 9: Map</em></div><br>
- The map is hard coding in python. This is the example of maze that have 9x9 dimension.<br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/findend.PNG"></div>
<div align="center"><em>Figure 10: Path Planning Algorithm: Breadth First Search</em></div><br>
- 

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/result.PNG"></div>
<div align="center"><em>Figure 11: Path Planning Result</em></div><br>
- The red color plus symbol shows the path to criminal and white hash symbol shows the building

:stars: **Project Result**
- Our results contain of labeled face with its confidence level. Figure below shows our system results:

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Aiman_Capture.JPG"></div>
<div align="center"><em>Figure 12: Aiman face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Ariff_Capture.JPG"></div>
<div align="center"><em>Figure 13: Ariff face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Azri_Capture.JPG"></div>
<div align="center"><em>Figure 14: Azri face result</em></div><br>

<div align="center"><img src="https://github.com/azri41/iCrime/blob/main/images/Izz_Capture.JPG"></div>
<div align="center"><em>Figure 15: Haziq face result</em></div><br>

## E. COMPLETING THE PROJECT

:clipboard: **Closing Checklist**
<br>
:heavy_check_mark: [Sign Off](https://github.com/azri41/iCrime/blob/main/images/SignOff.PNG)
<br>
:heavy_check_mark: [Lesson Learned](https://github.com/azri41/iCrime/blob/main/Lab%20and%20project%20progress/Project%20Closing%20iCrime.pdf)
<br>
:heavy_check_mark: [Final Project Report](https://github.com/azri41/iCrime/blob/main/README.md)
<br>
:heavy_check_mark: [Close Contract](https://github.com/azri41/iCrime/blob/main/Lab%20and%20project%20progress/iCrime%20Procurement%20Management%20Plan.pdf)
<br>

## F. PROJECT PRESENTATION

- [ ] [Embed youtube video] or [insert your youtube video link like the example below]

[![Ideaku](https://img.youtube.com/vi/1ByNYN1LQAI/0.jpg)](http://www.youtube.com/watch?v=1ByNYN1LQAI "Ideaku")
