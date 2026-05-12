# 📊 Teacher Dashboard - Visual Flow Diagram

## Complete Flow - From Start to Finish

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    TEACHER DASHBOARD - ATTENDANCE FLOW                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────┐
                              │  Teacher Login  │
                              └────────┬────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────┐
                      │  Teacher Dashboard Loaded      │
                      │  ✨ Welcome, [Teacher Name]   │
                      └────────────────────────────────┘
                                       │
                                       ▼
                      ┌────────────────────────────────┐
                      │ Generate Attendance Code       │
                      │ • Set Duration (1-5 min)       │
                      │ • Click [Generate Button]      │
                      └────────┬───────────────────────┘
                               │
                               ▼
        ┌──────────────────────────────────────────────────────┐
        │ Code Generated: ABC123                              │
        │ Expires in: 5:00                                    │
        │ Share with students →                               │
        └──────────────────────────────────────────────────────┘
                               │
                               │ (Students see code, log in)
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
        ┌──────────────────┐         ┌──────────────────┐
        │  Student 1       │         │  Student 2       │
        │  • Enters code   │         │  • Enters code   │
        │  • Captures face │         │  • Captures face │
        │  • Verified ✅   │         │  • Verified ✅   │
        └────────┬─────────┘         └────────┬─────────┘
                 │                            │
                 │ (Attendance marked)        │
                 │                            │
                 └──────────────┬─────────────┘
                                │
                                ▼
        ┌───────────────────────────────────────────────────────┐
        │                                                       │
        │  TEACHER SEES REAL-TIME UPDATE (Every 5 seconds)    │
        │                                                       │
        │  ┌─────────────────────────────────────────────────┐ │
        │  │ Live Attendance                   ✅ 2 marked  │ │
        │  │ ┌──────────────┬──────────┬─────┬──────┬────────┐ │
        │  │ │ # │ Name     │ Branch   │ Sem │Time │Status  │ │
        │  │ ├───┼──────────┼──────────┼─────┼─────┼────────┤ │
        │  │ │ 1 │John Doe  │ CSE      │ 4   │10:15│✅ Veri.│ │
        │  │ │ 2 │Jane Smith│ CSE      │ 4   │10:16│✅ Veri.│ │
        │  │ └──────────────┴──────────┴─────┴──────┴────────┘ │
        │  │                                                    │
        │  │ ┌─────────────────────────────────────────────────┐ │
        │  │ │ Absent Students              ❌ 20 absent       │ │
        │  │ │ ┌──────────────┬──────────┬─────────────────┐  │ │
        │  │ │ │ # │ Name     │ Branch   │ Sem            │  │ │
        │  │ │ ├───┼──────────┼──────────┼────────────────┤  │ │
        │  │ │ │ 1 │Alice Wang│ CSE      │ 4             │  │ │
        │  │ │ │ 2 │Bob Jones │ ECE      │ 4             │  │ │
        │  │ │ │ 3 │Charlie B.│ CSE      │ 3             │  │ │
        │  │ │ │...│ ... (17 more)                      │  │ │
        │  │ │ └──────────────┴──────────┴────────────────┘  │ │
        │  └─────────────────────────────────────────────────┘ │
        │                                                       │
        └───────────────────────────────────────────────────────┘

                (More students continue marking...)

        ┌──────────────────────────────────────────────────────┐
        │                                                       │
        │  SESSION IN PROGRESS - REAL-TIME UPDATES             │
        │                                                       │
        │  Every 5 seconds:                                    │
        │  • New present students added to top table           │
        │  • Marked students removed from absent list          │
        │  • Counts updated (✅ Present +1, ❌ Absent -1)      │
        │  • Tables refresh automatically                      │
        │                                                       │
        │  Teacher can:                                        │
        │  ✓ See who has marked (with timestamps)              │
        │  ✓ See who is still missing                          │
        │  ✓ Verify face recognition success                  │
        │  ✓ Encourage absent students                         │
        │                                                       │
        └───────────────────────────────────────────────────────┘

                    (Time passes... 4:00 remaining)

        ┌──────────────────────────────────────────────────────┐
        │ Final Status:                                         │
        │ ✅ Present: 18 students (rows 1-18)                  │
        │ ❌ Absent:  4 students (rows 1-4)                    │
        │ Total: 22 students                                   │
        └──────────────────────────────────────────────────────┘

                    (More students mark... 2:00 remaining)

        ┌──────────────────────────────────────────────────────┐
        │ Updated Status:                                       │
        │ ✅ Present: 20 students                              │
        │ ❌ Absent:  2 students (Alice Wang, Henry Park)      │
        │ Total: 22 students                                   │
        └──────────────────────────────────────────────────────┘

                        (Session expires 0:00)

        ┌──────────────────────────────────────────────────────┐
        │ ⏱️  SESSION EXPIRED                                   │
        │                                                       │
        │ Final Attendance:                                    │
        │ ✅ Present:  20 students                             │
        │ ❌ Absent:   2 students                              │
        │ Percentage: 90.9%                                    │
        │                                                       │
        │ Views are now FROZEN (read-only)                     │
        │ Teacher can review and generate new code             │
        └──────────────────────────────────────────────────────┘

                              │
                              ▼
                    (Teacher generates new code for next class)

```

---

## Parallel View - What Students See

```
STUDENT PERSPECTIVE                 TEACHER SEES IN REAL-TIME
═══════════════════════════════════════════════════════════════

Student 1:                          (Code ABC123 generated)
 • Logs in
 • Enters: ABC123
 • Camera opens                      
 • Captures face
 • "Verifying..."                    Polling starts...
 • ✅ "Attendance marked!"
                                     ▼ (Update #1)
Student 2:                          Present: John Doe
 • Logs in
 • Enters: ABC123                    Absent: 21 others
 • Camera opens
 • Captures face
 • "Verifying..."                    ▼ (Update #2)
 • ✅ "Attendance marked!"
                                     Present: John Doe, Jane Smith
Student 3:                          Absent: 20 others
 • Still entering code...
 • ...
                                     ▼ (Update #3, #4, #5...)
```

---

## Dashboard 2-Column Layout

```
┌──────────────────────────────────────────────────────────────────┐
│                     TEACHER DASHBOARD                            │
├────────────────────────────────┬────────────────────────────────┤
│                                │                                │
│  ⚡ GENERATE SESSION CODE      │  ✅ LIVE ATTENDANCE           │
│  ┌──────────────────────────┐ │  ┌────────────────────────────┐
│  │ Duration:                │ │  │ Marked: 15                 │
│  │ [●●●●●○○○○] 1 min       │ │  │ ┌──────────────────────────┐
│  │                          │ │  │ │ # │Name │Branch │...│    │
│  │ [Generate Code]          │ │  │ ├────────────────────┤    │
│  │                          │ │  │ │ 1 │John │ CSE    │...│    │
│  │ Code: ABC123 📋          │ │  │ │ 2 │Jane │ CSE    │...│    │
│  │                          │ │  │ │ 3 │Bob  │ ECE    │...│    │
│  │ Expires in: 3:45         │ │  │ │...│ ... │ ...    │...│    │
│  │ [████████░░░░░░░░░░░░░░]│ │  │ └──────────────────────────┘
│  └──────────────────────────┘ │  └────────────────────────────┘
│                                │
├────────────────────────────────┴────────────────────────────────┤
│                                                                  │
│  ❌ ABSENT STUDENTS                                             │
│  ┌──────────────────────────────────────────────────────────────┐
│  │ Absent: 7                                                    │
│  │ ┌──────────────────────────────────────────────────────────┐ │
│  │ │ # │ Name       │ Branch  │ Sem                           │ │
│  │ ├────────────────────────────────────────────────────────┤ │
│  │ │ 1 │ Alice Wang │ CSE     │ 4                           │ │
│  │ │ 2 │ Charlie B. │ CSE     │ 3                           │ │
│  │ │ 3 │ David Lee  │ ECE     │ 4                           │ │
│  │ │ 4 │ Emma Davis │ CSE     │ 4                           │ │
│  │ │ 5 │ Frank Mll. │ MECH    │ 4                           │ │
│  │ │ 6 │ Grace Lee  │ CSE     │ 4                           │ │
│  │ │ 7 │ Henry Park │ ECE     │ 3                           │ │
│  │ └──────────────────────────────────────────────────────────┘ │
│  └──────────────────────────────────────────────────────────────┘
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## State Transitions

```
                    Initial State
                         │
                         ▼
            ┌─────────────────────────┐
            │ No Code Generated       │
            │ • Present: Empty        │
            │ • Absent: All students  │
            └────────────┬────────────┘
                         │ [Generate Button]
                         ▼
            ┌─────────────────────────┐
            │ Code Generated          │
            │ • Timer: 5:00           │
            │ • Polling starts        │
            └────────────┬────────────┘
                         │ [Students mark attendance]
                         ▼
            ┌─────────────────────────┐
            │ Active Session          │
            │ • Present grows         │
            │ • Absent shrinks        │
            │ • Updates every 5s      │
            └────────────┬────────────┘
                         │ [Timer 0:00]
                         ▼
            ┌─────────────────────────┐
            │ Session Expired         │
            │ • Views frozen          │
            │ • Final attendance set  │
            │ • Polling stops         │
            └────────────┬────────────┘
                         │ [Generate new code]
                         └─────────── (back to start)
```

---

## Data Flow

```
┌──────────────┐
│ Teacher      │
│ Dashboard    │
└───────┬──────┘
        │ Generates Code
        ▼
┌──────────────────┐
│ API: Generate    │
│ Attendance       │
└───────┬──────────┘
        │ Returns: session_id, code, expires_at
        ▼
┌──────────────────────────────────┐
│ Start Polling Every 5 Seconds    │
│ GET /attendance-status           │
└───────┬──────────────────────────┘
        │
        ├─── Poll 1: 0 present, 22 absent
        │
        ├─── Poll 2: 2 present, 20 absent
        │
        ├─── Poll 3: 5 present, 17 absent
        │
        └─── ... (continues until session expires)

        When Session Expires:
        └─── Polling stops
             Final counts frozen
```

---

## Color Legend

```
Tables:
├─ Present (Live Attendance):
│  └─ Normal white background (students are here)
│
└─ Absent:
   └─ Light red background (students are missing)

Badges:
├─ ✅ Green: Face verified successfully
├─ ❌ Red: Not verified / Manual
└─ ❌ Red badge: Absent count
```

---

## Summary

**Before:** Teachers could only see who marked attendance  
**After:** Teachers can see BOTH who marked AND who didn't  

This allows them to:
- ✅ Know attendance status immediately
- ✅ Identify absent students
- ✅ Send reminders in real-time
- ✅ Monitor system reliability
- ✅ Improve class participation

