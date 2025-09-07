import React, { useState } from 'react'
import DataEntry from './pages/DataEntry'
import Scheduler from './pages/Scheduler'

export default function App(){
  const [tab, setTab] = useState('data')
  return (
    <div className="p-6 space-y-6">
      <header className="max-w-6xl mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Smart Classroom</h1>
        <nav className="flex gap-2">
          <button onClick={()=>setTab('data')} className={"px-3 py-2 rounded-2xl " + (tab==='data'?'bg-black text-white':'bg-white shadow')}>Data</button>
          <button onClick={()=>setTab('scheduler')} className={"px-3 py-2 rounded-2xl " + (tab==='scheduler'?'bg-black text-white':'bg-white shadow')}>Scheduler</button>
        </nav>
      </header>
      {tab==='data' ? <DataEntry /> : <Scheduler />}
      <footer className="text-center text-xs text-gray-500 pt-8">Starter kit • Customize freely</footer>
    </div>
  )
}
