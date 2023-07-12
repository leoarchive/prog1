from datetime import date
import pickle
from cliente import Cliente
from animal import Animal, Cao, Gato, Passaro
from produto import Produto
from servico import Servico, Banho, Tosa, ConsultaVeterinaria
from agendamento import Agendamento

gato='  /\_/\  ( \n\
 ( ^.^ ) _) \n\
   \\"/  (\n\
 ( | | )\n\
(__d b__)'

print(gato,'Pet Shop ProgramaCão!')

print('\nClientes:')
cliente_leonardo=Cliente('Leonardo',1,'000.000.000-00','Av. Python')
cliente_cristiano=Cliente('Cristiano',2,'111.111.111-11','Av. C')
[print('\t',cliente) for cliente in Cliente.clientes]

print('\nAnimais:')
animal_leonardo=Gato('Vira lata','Garfield',cliente_leonardo)
animal_cristiano=Cao('Poodle','Coragem',cliente_cristiano)
[print('\t',animal) for animal in Animal.animais]

print('\nProdutos:')
produto_racao=Produto('Ração para filhotes',1,20)
mata_pulgas=Produto('Mata Pulgas',2)
[print('\t',produto) for produto in Produto.produtos]

print('\nServiços:')
servico_banho=Banho()
servico_tosa=Tosa()
servico_consulta=ConsultaVeterinaria()
print('\tServiços disponíveis no PetShop: Tosa, Banho e Consultas Veterinárias!')

print('\nAgendamentos:')
agen_banho_leonardo=Agendamento(cliente_leonardo,animal_leonardo,servico_banho,date.today())
agen_tosa_cristiano=Agendamento(cliente_cristiano,animal_cristiano,servico_tosa,date.today())
[print('\t',agendamento) for agendamento in Agendamento.agendamentos]

print('\nSobrecarga (filtrando produtos):')
[print('\t',produto) for produto in Produto.filtrar(nome='Mata Pulgas')]

print('\nSobreposição:')
[print('\t',fala) for fala in [animal_leonardo.falar(),animal_cristiano.falar()]]

print('\nSerialização (pickle):')
print('\tSalvando Clientes...',end='')
with open('clientes.pkl', 'wb') as f:
  pickle.dump(Cliente.clientes, f)
  print(' ok')

print('\tSalvando Animais...',end='')
with open('animais.pkl', 'wb') as f:
  pickle.dump(Animal.animais, f)
  print(' ok')

print('\tSalvando Produtos...',end='')
with open('produtos.pkl', 'wb') as f:
  pickle.dump(Produto.produtos, f)
  print(' ok')

print('\tSalvando Agendamentos...',end='')
with open('agendamentos.pkl', 'wb') as f:
  pickle.dump(Agendamento.agendamentos, f)
  print(' ok')

print('\nDesserialização (pickle):')
print('\tCarregando Clientes... ',end='')
with open('clientes.pkl', 'rb') as f:
  print(pickle.load(f))

print('\tCarregando Animais... ',end='')
with open('animais.pkl', 'rb') as f:
  print(pickle.load(f))

print('\tCarregando Produtos... ',end='')
with open('produtos.pkl', 'rb') as f:
  print(pickle.load(f))

print('\tCarregando Agendamentos... ',end='')
with open('agendamentos.pkl', 'rb') as f:
  print(pickle.load(f))
