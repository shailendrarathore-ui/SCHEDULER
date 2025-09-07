import React, { useState, useEffect } from 'react'
import { get, post } from '../api'

function Section({ title, children }){
  return (
    <div className="bg-white p-4 rounded-2xl shadow mb-6">
      <h2 className="text-lg font-semibold mb-3">{title}</h2>
      {children}
    </div>
  )
}

export default function DataEntry(){
  const [teachers, setTeachers] = useState([])
  const [rooms, setRooms] = useState([])
  const [subjects, setSubjects] = useState([])
  const [timeslots, setTimeslots] = useState([])

  const reload = async () => {
    const [t,r,s,ts] = await Promise.all([
      get('/teachers/'),
      get('/rooms/'),
      get('/subjects/'),
      get('/timeslots/'),
    ])
    setTeachers(t); setRooms(r); setSubjects(s); setTimeslots(ts)
  }

  useEffect(() => { reload() }, [])

  const onAdd = async (path, body) => { await post(path, body); reload() }

  return (
    <div className="max-w-5xl mx-auto">
      <Section title="Teachers">
        <div className="flex gap-2 items-center">
          <input id="tname" className="border p-2 rounded w-64" placeholder="e.g., Ms. A" />
          <button className="px-3 py-2 rounded bg-black text-white" onClick={()=>onAdd('/teachers/', { name: document.getElementById('tname').value })}>Add</button>
        </div>
        <ul className="mt-3 text-sm text-gray-700 list-disc pl-6">
          {teachers.map(t => <li key={t.id}>{t.name}</li>)}
        </ul>
      </Section>

      <Section title="Rooms">
        <div className="flex gap-2 items-center flex-wrap">
          <input id="rname" className="border p-2 rounded w-48" placeholder="e.g., R101" />
          <label className="text-sm flex items-center gap-1"><input type="checkbox" id="rproj" /> Projector</label>
          <label className="text-sm flex items-center gap-1"><input type="checkbox" id="rlab" /> Lab</label>
          <button className="px-3 py-2 rounded bg-black text-white" onClick={()=>onAdd('/rooms/', { name: document.getElementById('rname').value, has_projector: document.getElementById('rproj').checked, is_lab: document.getElementById('rlab').checked })}>Add</button>
        </div>
        <ul className="mt-3 text-sm text-gray-700 list-disc pl-6">
          {rooms.map(r => <li key={r.id}>{r.name} {r.has_projector ? '(Projector)' : ''} {r.is_lab ? '(Lab)' : ''}</li>)}
        </ul>
      </Section>

      <Section title="Subjects">
        <div className="flex gap-2 items-center flex-wrap">
          <input id="sname" className="border p-2 rounded w-64" placeholder="e.g., Physics" />
          <label className="text-sm flex items-center gap-1"><input type="checkbox" id="slab" /> Requires Lab</label>
          <button className="px-3 py-2 rounded bg-black text-white" onClick={()=>onAdd('/subjects/', { name: document.getElementById('sname').value, requires_lab: document.getElementById('slab').checked })}>Add</button>
        </div>
        <ul className="mt-3 text-sm text-gray-700 list-disc pl-6">
          {subjects.map(s => <li key={s.id}>{s.name} {s.requires_lab ? '(Lab)' : ''}</li>)}
        </ul>
      </Section>

      <Section title="Time Slots">
        <div className="flex gap-2 items-center flex-wrap">
          <input id="tslabel" className="border p-2 rounded w-64" placeholder="e.g., Mon-09:00" />
          <input id="tsday" type="number" className="border p-2 rounded w-28" placeholder="day_index (0-6)" />
          <input id="tsslot" type="number" className="border p-2 rounded w-28" placeholder="slot_index (0..N)" />
          <button className="px-3 py-2 rounded bg-black text-white" onClick={()=>onAdd('/timeslots/', { label: document.getElementById('tslabel').value, day_index: Number(document.getElementById('tsday').value), slot_index: Number(document.getElementById('tsslot').value) })}>Add</button>
        </div>
        <ul className="mt-3 text-sm text-gray-700 list-disc pl-6">
          {timeslots.map(ts => <li key={ts.id}>{ts.label} (day {ts.day_index}, slot {ts.slot_index})</li>)}
        </ul>
      </Section>
    </div>
  )
}
