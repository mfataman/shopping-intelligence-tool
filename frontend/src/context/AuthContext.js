import React, { createContext, useContext, useEffect, useState } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const unsubscribe = () => {
            // Logic to unsubscribe from an authentication service
        };

        const fetchUser = () => {
            // Fetch the user from authentication service
            // On success:
            // setUser(fetchedUser);
            // On failure:
            // setUser(null);
        };

        fetchUser();
        return unsubscribe;
    }, []);

    return (
        <AuthContext.Provider value={{ user, loading }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};