import React, { useState } from 'react';
import axios from 'axios';
import EntropyChart from './EntropyChart';

export default function KeyGenerator() {
  const [keyData, setKeyData] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateKey = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/generate', {
        entropy_threshold: 7.5
      });
      setKeyData(response.data);
    } catch (err) {
      console.error('Ошибка при генерации ключа:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-gray-800 p-6 rounded-2xl shadow-xl">
      <button
        onClick={generateKey}
        className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-xl font-semibold"
      >
        {loading ? 'Генерация...' : 'Сгенерировать ключ'}
      </button>

      {keyData && (
        <div className="mt-6">
          <h3 className="text-xl font-semibold mb-2">🔐 HEX-ключ:</h3>
          <p className="break-all text-green-400 bg-gray-900 p-2 rounded mb-4">
            {keyData.key_hex}
          </p>

          <div className="space-y-2">
            <p>📈 Энтропия: <strong>{keyData.entropy}</strong></p>
            <p>📉 Мин. энтропия: <strong>{keyData.min_entropy}</strong></p>
            <p>⚖️ Баланс битов: 0 → {keyData.bit_ratio['0']}, 1 → {keyData.bit_ratio['1']}</p>
            <p>
              ✅ NIST-тест: <strong className={keyData.nist_passed ? 'text-green-500' : 'text-red-500'}>
                {keyData.nist_passed ? 'Пройден' : 'Не пройден'}
              </strong>
            </p>
          </div>

          <div className="mt-6">
            <EntropyChart entropy={keyData.entropy} minEntropy={keyData.min_entropy} />
          </div>
        </div>
      )}
    </div>
  );
}
