from ortools.sat.python import cp_model

def generate_schedule(subjects, teachers, rooms, timeslots):
    # Minimal toy model:
    # Assumptions: len(subjects) <= len(timeslots)
    model = cp_model.CpModel()
    # Variables: x[s,t,r,ts] in {0,1}
    X = {}
    for s in subjects:
        for t in teachers:
            for r in rooms:
                for ts in timeslots:
                    X[(s['id'], t['id'], r['id'], ts['id'])] = model.NewBoolVar(f"x_{s['id']}_{t['id']}_{r['id']}_{ts['id']}")

    # Each subject exactly once
    for s in subjects:
        model.Add(sum(X[(s['id'], t['id'], r['id'], ts['id'])] for t in teachers for r in rooms for ts in timeslots) == 1)

    # One class per teacher per timeslot
    for t in teachers:
        for ts in timeslots:
            model.Add(sum(X[(s['id'], t['id'], r['id'], ts['id'])] for s in subjects for r in rooms) <= 1)

    # One class per room per timeslot
    for r in rooms:
        for ts in timeslots:
            model.Add(sum(X[(s['id'], t['id'], r['id'], ts['id'])] for s in subjects for t in teachers) <= 1)

    # Optional: subjects requiring lab must be placed into lab rooms
    for s in subjects:
        if s.get("requires_lab"):
            for t in teachers:
                for r in rooms:
                    if not r.get("is_lab"):
                        for ts in timeslots:
                            model.Add(X[(s['id'], t['id'], r['id'], ts['id'])] == 0)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return []

    schedule = []
    for s in subjects:
        for t in teachers:
            for r in rooms:
                for ts in timeslots:
                    if solver.Value(X[(s['id'], t['id'], r['id'], ts['id'])]) == 1:
                        schedule.append({
                            "subject_id": s["id"],
                            "teacher_id": t["id"],
                            "room_id": r["id"],
                            "timeslot_id": ts["id"],
                        })
    return schedule
