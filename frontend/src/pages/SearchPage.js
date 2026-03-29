import React, { useState } from 'react';

const SearchPage = () => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);

    const handleSearch = () => {
        // Simulate an API call to fetch products based on the query
        const fetchedResults = [
            { id: 1, name: 'Product 1' },
            { id: 2, name: 'Product 2' },
            { id: 3, name: 'Product 3' },
        ];
        setResults(fetchedResults.filter(product => product.name.toLowerCase().includes(query.toLowerCase())));
    };

    return (
        <div>
            <h1>Product Search</h1>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search for products..."
            />
            <button onClick={handleSearch}>Search</button>
            <ul>
                {results.map(product => (
                    <li key={product.id}>{product.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default SearchPage;