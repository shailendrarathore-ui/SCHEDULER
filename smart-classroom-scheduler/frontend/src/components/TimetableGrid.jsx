import React from 'react'

export default function TimetableGrid({ assignments }) {
  // Build grid by day and slot_index
  const days = [...new Set(assignments.map(a => a.day_index))].sort((a,b)=>a-b)
  const slots = [...new Set(assignments.map(a => a.slot_index))].sort((a,b)=>a-b)

  const cell = (d, s) => assignments.find(a => a.day_index === d && a.slot_index === s)

  return (
    <div className="overflow-auto">
      <table className="min-w-full border border-gray-200 bg-white rounded-xl shadow">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">Slot \ Day</th>
            {days.map(d => <th key={d} className="p-2 border">Day {d}</th>)}
          </tr>
        </thead>
        <tbody>
          {slots.map(s => (
            <tr key={s}>
              <td className="p-2 border font-medium">Slot {s}</td>
              {days.map(d => {
                const a = cell(d,s)
                return (
                  <td key={d} className="p-2 border align-top">
                    {a ? (
                      <div className="space-y-1">
                        <div className="text-sm font-semibold">{a.subject}</div>
                        <div className="text-xs text-gray-600">Teacher: {a.teacher}</div>
                        <div className="text-xs text-gray-600">Room: {a.room}</div>
                        <div className="text-[10px] text-gray-500">{a.timeslot}</div>
                      </div>
                    ) : <span className="text-gray-300 text-sm">—</span>}
                  </td>
                )
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
