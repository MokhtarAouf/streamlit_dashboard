
    import { useState } from 'react';
    import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
    import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
    import { PieChart, Pie, Cell, Legend, ResponsiveContainer, Tooltip } from 'recharts';

    const PathologyDistribution = () => {
      const [selectedYear, setSelectedYear] = useState('2022');
      
      const data = {"2015": [{"name": "Maladies cardioneurovasculaires", "value": 21.93}, {"name": "Traitements psychotropes (hors pathologies)", "value": 17.43}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 14.75}, {"name": "Cancers", "value": 12.31}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.41}, {"name": "Maladies neurologiques", "value": 5.49}, {"name": "Maladies psychiatriques", "value": 5.03}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.52}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.4}, {"name": "Diabète", "value": 3.34}], "2016": [{"name": "Maladies cardioneurovasculaires", "value": 22.45}, {"name": "Traitements psychotropes (hors pathologies)", "value": 17.0}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 14.25}, {"name": "Cancers", "value": 12.3}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.53}, {"name": "Maladies neurologiques", "value": 5.52}, {"name": "Maladies psychiatriques", "value": 5.11}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.55}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.47}, {"name": "Diabète", "value": 3.4}], "2017": [{"name": "Maladies cardioneurovasculaires", "value": 22.85}, {"name": "Traitements psychotropes (hors pathologies)", "value": 16.39}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.83}, {"name": "Cancers", "value": 12.52}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.54}, {"name": "Maladies neurologiques", "value": 5.58}, {"name": "Maladies psychiatriques", "value": 5.25}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.57}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.56}, {"name": "Diabète", "value": 3.46}], "2018": [{"name": "Maladies cardioneurovasculaires", "value": 23.02}, {"name": "Traitements psychotropes (hors pathologies)", "value": 15.86}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.54}, {"name": "Cancers", "value": 12.77}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.61}, {"name": "Maladies neurologiques", "value": 5.58}, {"name": "Maladies psychiatriques", "value": 5.41}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.65}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.57}, {"name": "Diabète", "value": 3.51}], "2019": [{"name": "Maladies cardioneurovasculaires", "value": 23.17}, {"name": "Traitements psychotropes (hors pathologies)", "value": 15.4}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.34}, {"name": "Cancers", "value": 12.95}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.64}, {"name": "Maladies psychiatriques", "value": 5.6}, {"name": "Maladies neurologiques", "value": 5.54}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.75}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.61}, {"name": "Diabète", "value": 3.57}], "2020": [{"name": "Maladies cardioneurovasculaires", "value": 23.14}, {"name": "Traitements psychotropes (hors pathologies)", "value": 15.78}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.42}, {"name": "Cancers", "value": 13.06}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 8.74}, {"name": "Maladies psychiatriques", "value": 5.48}, {"name": "Maladies neurologiques", "value": 5.47}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.83}, {"name": "Diabète", "value": 3.64}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.63}], "2021": [{"name": "Maladies cardioneurovasculaires", "value": 22.94}, {"name": "Traitements psychotropes (hors pathologies)", "value": 15.82}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.41}, {"name": "Cancers", "value": 12.98}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.25}, {"name": "Maladies neurologiques", "value": 5.34}, {"name": "Maladies psychiatriques", "value": 5.33}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.87}, {"name": "Diabète", "value": 3.69}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.58}], "2022": [{"name": "Maladies cardioneurovasculaires", "value": 22.82}, {"name": "Traitements psychotropes (hors pathologies)", "value": 15.58}, {"name": "Traitements du risque vasculaire (hors pathologies)", "value": 13.5}, {"name": "Cancers", "value": 12.9}, {"name": "Hospitalisations hors pathologies repérées (avec ou sans pathologies, traitements ou maternité)", "value": 9.46}, {"name": "Maladies neurologiques", "value": 5.31}, {"name": "Maladies psychiatriques", "value": 5.3}, {"name": "Maladies inflammatoires ou rares ou infection VIH", "value": 3.94}, {"name": "Diabète", "value": 3.82}, {"name": "Maladies respiratoires chroniques (hors mucoviscidose)", "value": 3.66}]};

      const COLORS = [
        '#1e40af', // Dark blue
        '#60a5fa', // Light blue
        '#ef4444', // Red
        '#fca5a5', // Light red
        '#10b981', // Green
        '#86efac', // Light green
        '#f97316', // Orange
        '#fb923c', // Light orange
        '#6366f1', // Indigo
        '#a5b4fc'  // Light indigo
      ];

      const handleYearChange = (value) => {
        setSelectedYear(value);
      };

      const CustomTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
          return (
            <div className="bg-white p-4 rounded shadow border">
              <p className="font-medium">{payload[0].name}</p>
              <p className="text-gray-600">{`${payload[0].value.toFixed(1)}%`}</p>
            </div>
          );
        }
        return null;
      };

      return (
        <Card className="w-full max-w-4xl">
          <CardHeader>
            <div className="flex justify-between items-center">
              <CardTitle>Top 10 Pathologies Distribution</CardTitle>
              <Select value={selectedYear} onValueChange={handleYearChange}>
                <SelectTrigger className="w-32">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {Object.keys(data).map((year) => (
                    <SelectItem key={year} value={year}>
                      {year}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          </CardHeader>
          <CardContent>
            <div className="h-[600px] w-full">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={data[selectedYear]}
                    cx="50%"
                    cy="50%"
                    labelLine={true}
                    label={({ name, percent }) => `${name} (${(percent * 100).toFixed(1)}%)`}
                    outerRadius={200}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {data[selectedYear].map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip content={<CustomTooltip />} />
                  <Legend layout="vertical" align="right" verticalAlign="middle" />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>
      );
    };

    export default PathologyDistribution;
    