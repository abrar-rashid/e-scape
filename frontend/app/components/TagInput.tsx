import React, { useState } from 'react';

const TagInput: React.FC<{ tags: string[]; onChange: (tags: string[]) => void }> = ({ tags, onChange }) => {
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleInputKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && inputValue.trim() !== '') {
      e.preventDefault();
      const newTags = [...tags, inputValue.trim()];
      onChange(newTags);
      setInputValue('');
    }
  };

  const handleTagRemove = (index: number) => {
    const newTags = [...tags.slice(0, index), ...tags.slice(index + 1)];
    onChange(newTags);
  };

  return (
    <div>
        <input
            type="text"
            value={inputValue}
            onChange={handleInputChange}
            onKeyDown={handleInputKeyDown}
            placeholder="Keywords"
            className="border border-gray-300 rounded-md text-center px-3 py-1.5 mt-2 mb-5 w-80 text-black"
        />
        <div>
            {tags.map((tag, index) => (
            <div key={index} className="inline-block bg-white rounded-md px-3 py-1 mr-2 mb-5 flex-wrap text-black">
                {tag}
                <button
                className="ml-1 text-xs text-gray-500"
                onClick={() => handleTagRemove(index)}
                >
                X
                </button>
            </div>
            ))}
        </div>

    </div>
  );
};

export default TagInput;
