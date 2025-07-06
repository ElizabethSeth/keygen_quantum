import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend,
} from 'recharts';

export default function EntropyChart({ entropy, minEntropy }) {
  const data = [
    {
      name: 'Shannon Entropy', value: entropy,
    },
    {
      name: 'Min Entropy', value: minEntropy,
    },
  ];

  return (
    <div className="bg-gradient-to-br from-gray-800 to-gray-900 p-6 rounded-2xl shadow-lg border border-gray-700">
      <h4 className="text-2xl font-semibold mb-4 text-center text-blue-400">
        🔎 Анализ Энтропии
      </h4>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="4 4" stroke="#444" />
          <XAxis dataKey="name" stroke="#ccc" fontSize={12} />
          <YAxis domain={[0, 8]} stroke="#ccc" fontSize={12} />
          <Tooltip contentStyle={{ backgroundColor: '#1f2937', color: '#fff', borderRadius: '8px' }} />
          <Legend wrapperStyle={{ color: '#ccc' }} />
          <Bar dataKey="value" fill="#60a5fa" radius={[8, 8, 0, 0]} barSize={60} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
