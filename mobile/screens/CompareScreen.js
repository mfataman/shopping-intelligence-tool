import React from 'react';
import { View, Text, StyleSheet, Button } from 'react-native';

const CompareScreen = () => {
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Price Comparison</Text>
            <View style={styles.comparisonContainer}>
                {/* Add your comparisons here */}
                <Text style={styles.comparisonText}>Product A: $50</Text>
                <Text style={styles.comparisonText}>Product B: $45</Text>
                <Text style={styles.comparisonText}>Product C: $55</Text>
            </View>
            <Button title="Compare Prices" onPress={() => {}} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
    },
    title: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 20,
    },
    comparisonContainer: {
        width: '100%',
        marginBottom: 20,
    },
    comparisonText: {
        fontSize: 18,
        marginVertical: 5,
    },
});

export default CompareScreen;