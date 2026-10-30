'use client';
import React, { useState } from 'react';

export default function CameraCapture({ onCapture }: { onCapture: (url: string) => void }) {
  const [imageUrl, setImageUrl] = useState('');

  const handleScan = () => {
    const sampleUrl = imageUrl || "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80";
    onCapture(sampleUrl);
  };

  return (
    <div className="p-6 bg-slate-900 text-white rounded-xl shadow-lg max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">AuraStudio Vision Capture</h2>
      <input
        type="text"
        placeholder="Enter image URL for diagnostic"
        value={imageUrl}
        onChange={(e) => setImageUrl(e.target.value)}
        className="w-full p-2 mb-4 bg-slate-800 border border-slate-700 rounded text-sm text-white placeholder-slate-400"
      />
      <button
        onClick={handleScan}
        className="w-full bg-indigo-600 hover:bg-indigo-500 font-semibold py-2 px-4 rounded transition cursor-pointer"
      >
        Run Skin & VTO Diagnostic
      </button>
    </div>
  );
}
