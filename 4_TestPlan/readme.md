# TEST PLAN:

| **ID** | **DESCRIPTION**
 | **EXPECTED INPUT** | **EXPECTED OUTPUT** | **ACTUAL OUTPUT** |
| --- | --- | --- | --- | --- |
| **LL\_1** | Top 5 students | [5.3,6,7,8,4,7.6,8.2] | Id of students whose averages are 5.3,6,7,8,4 |
 |
| **LL\_2** | Bottom 5 students | [5.3,6,7,8,4,7.6,8.2] | Id of students whose averages are 8.2,7.6,4,8,7 |
 |

| **ID** | **DESCRIPTION**
 | **EXPECTED INPUT** | **EXPECTED OUTPUT** | **ACTUAL OUTPUT** |
| --- | --- | --- | --- | --- |
| **HL\_1** | Average for one module | LO\_1 = 4,5,6,7 | Avg\_LO1 = 5.5 | **Above average** |
| **HL\_2** | Average of individual student | Averages of all module :[5.5,4,7,9,1] |
5.3 | **Above average** |
| **HL\_3** | Average of class | Average of individual student: [5.3,6,7,8,4,7.6,8.2] |
6.585 |
**Above average** |
| **HL\_4** | Failed | Average of individual student: [5.3,6,7,8,4,7.6,8.2] |
None |
**All passed** |
