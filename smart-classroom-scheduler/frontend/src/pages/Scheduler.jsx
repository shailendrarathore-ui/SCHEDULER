import React, { useState, useEffect } from 'react'
import { get, post } from '../api'
import TimetableGrid from '../components/TimetableGrid'

export default function Scheduler(){
  const [assignments, setAssignments] = useState([])
  const reload = async () => setAssignments(await get('/scheduler/assignments'))
  useEffect(()=>{ reload() }, [])

  const generate = async () => { await post('/scheduler/generate'); reload() }

  return (
    <div className="max-w-6xl mx-auto space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-semibold">Scheduler</h2>
        <button onClick={generate} className="px-4 py-2 rounded-2xl bg-black text-white shadow">Generate</button>
      </div>
      <TimetableGrid assignments={assignments} />
    </div>
  )
}
