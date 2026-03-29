import React, { createContext, useState, useEffect } from 'react';

const ProductContext = createContext();

export const ProductProvider = ({ children }) => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchProducts = async (query) => {
        setLoading(true);
        try {
            const response = await fetch(`https://api.example.com/products?search=${query}`);
            const data = await response.json();
            setProducts(data);
        } catch (err) {
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchProducts('initial search'); // Replace with dynamic search as needed
    }, []);

    return (
        <ProductContext.Provider value={{ products, loading, error, fetchProducts }}>
            {children}
        </ProductContext.Provider>
    );
};

export const useProductContext = () => {
    return React.useContext(ProductContext);
};
