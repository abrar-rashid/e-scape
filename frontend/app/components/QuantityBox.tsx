// QuantityBox.tsx
import React from 'react';

interface QuantityBoxProps {
    value: number;
    onChange: (value: number) => void;
}

const QuantityBox: React.FC<QuantityBoxProps> = ({ value, onChange }) => {
    const increment = () => {
        onChange(value + 1);
    };

    const decrement = () => {
        if (value > 1) {
            onChange(value - 1);
        }
    };

    return (
        <div className="flex items-center justify-center">
            <button onClick={decrement} className="px-2 py-1 mt-2 mb-2 bg-gray-200 text-gray-600 rounded-l">
                -
            </button>
            <input type="number" value={value.toString()} onChange={e => onChange(parseInt(e.target.value))} className="px-2 mt-2 mb-2 py-1 items-center justify-center text-center bg-gray-100 text-black w-16" />
            <button onClick={increment} className="px-2 py-1 mt-2 mb-2 bg-gray-200 text-gray-600 rounded-r">
                +
            </button>
        </div>
    );
    
};

export default QuantityBox;
