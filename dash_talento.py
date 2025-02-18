import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { Users, Calendar, MessageCircle, Moon } from 'lucide-react';

const DashboardEducativo = () => {
  const [progreso, setProgreso] = useState(784);
  const [modo, setModo] = useState('claro');
  const [datosGrafica] = useState([
    { mes: 'Ene', valor: 30 },
    { mes: 'Feb', valor: 45 },
    { mes: 'Mar', valor: 35 },
    { mes: 'Abr', valor: 50 },
    { mes: 'May', valor: 40 }
  ]);

  const [estudiantes] = useState([
    { nombre: "Sarah Hudson", hora: "10:00", avatar: "/api/placeholder/30/30" },
    { nombre: "Dakota Smith", hora: "11:15", avatar: "/api/placeholder/30/30" },
    { nombre: "John Lane", hora: "12:30", avatar: "/api/placeholder/30/30" }
  ]);

  const [eventos] = useState([
    { tipo: "Reunión de equipo", participantes: 3 },
    { tipo: "Clase de arte", participantes: 2 }
  ]);

  return (
    <div className={`p-6 ${modo === 'oscuro' ? 'bg-gray-900 text-white' : 'bg-green-50'}`}>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Mi Tablero Mágico</h1>
        <button 
          onClick={() => setModo(modo === 'claro' ? 'oscuro' : 'claro')}
          className="p-2 rounded-full hover:bg-gray-200"
        >
          <Moon className="w-6 h-6" />
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Tarjeta de Progreso */}
        <Card className="bg-white shadow-lg">
          <CardHeader>
            <CardTitle className="text-lg">Progreso del Día</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center justify-center">
              <div className="relative w-32 h-32">
                <svg className="w-full h-full" viewBox="0 0 36 36">
                  <path
                    d="M18 2.0845
                      a 15.9155 15.9155 0 0 1 0 31.831
                      a 15.9155 15.9155 0 0 1 0 -31.831"
                    fill="none"
                    stroke="#eee"
                    strokeWidth="3"
                  />
                  <path
                    d="M18" 2.0845
                      a 15.9155 15.9155 0 0 1 0 31.831
                      a 15.9155 15.9155 0 0 1 0 -31.831"
                    fill="none"
                    stroke="#4CAF50"
                    strokeWidth="3"
                    strokeDasharray={`${(progreso / 1000) * 100}, 100`}
                  />
                  <text x="18" y="20.35" className="text-3xl font-bold text-center">
                    {progreso}
                  </text>
                </svg>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Tarjeta de Gráfica */}
        <Card className="bg-white shadow-lg">
          <CardHeader>
            <CardTitle className="text-lg">Actividades del Mes</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="h-48">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={datosGrafica}>
                  <XAxis dataKey="mes" />
                  <YAxis />
                  <Tooltip />
                  <Line 
                    type="monotone" 
                    dataKey="valor" 
                    stroke="#4CAF50" 
                    strokeWidth={2}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Lista de Estudiantes */}
        <Card className="bg-white shadow-lg">
          <CardHeader>
            <CardTitle className="text-lg">Amiguitos de Hoy</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {estudiantes.map((estudiante, index) => (
                <div key={index} className="flex items-center space-x-4">
                  <img 
                    src={estudiante.avatar} 
                    alt={estudiante.nombre}
                    className="w-8 h-8 rounded-full"
                  />
                  <div>
                    <p className="font-medium">{estudiante.nombre}</p>
                    <p className="text-sm text-gray-500">{estudiante.hora}</p>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        {/* Lista de Eventos */}
        <Card className="bg-white shadow-lg">
          <CardHeader>
            <CardTitle className="text-lg">Eventos Divertidos</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {eventos.map((evento, index) => (
                <div key={index} className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                  <span>{evento.tipo}</span>
                  <div className="flex items-center space-x-2">
                    <Users className="w-4 h-4" />
                    <span>{evento.participantes}</span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default DashboardEducativo;
