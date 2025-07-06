import React from 'react';
import KeyGenerator from './components/KeyGenerator';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-4 text-center">
          🧠 Post-Quantum Key Generator
        </h1>
        <p className="text-center mb-8 text-gray-400">
          Сгенерируй и проанализируй криптографические ключи с помощью ИИ
        </p>
        <KeyGenerator />
      </div>
    </div>
  );
}
