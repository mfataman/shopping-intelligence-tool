import React from 'react';

const PriceComparison = ({ prices }) => {
    return (
        <div className="price-comparison">
            <h2>Price Comparison</h2>
            <table>
                <thead>
                    <tr>
                        <th>Retailer</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {prices.map((priceData, index) => (
                        <tr key={index}>
                            <td>{priceData.retailer}</td>
                            <td>{priceData.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PriceComparison;