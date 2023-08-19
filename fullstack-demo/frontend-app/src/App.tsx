import './App.css'                                                    //é um arquivo .css que tem todas as definições de customização criadas que serão usadas
import { Layout, Row, Card, Col, message, Popconfirm } from 'antd'    //'antd' é uma biblioteca de de componentes pra UI, usada no framework React
import ButtonAdd from './components/addButton/addButton'
import { deleteItem, todosItems } from './services/apiFunctions'
import { itemType } from "./types/itemType";
import { useEffect, useState } from 'react';
import { DeleteOutlined } from '@ant-design/icons';

const { Header, Footer, Content } = Layout;                           //Header = Cabeçalho; Footer = Rodapé; Content = Body (conteúdo da página) -> todos importados de layout

function App() {                                                      //é uma função que tem os scripts (e que retorna (dentro do return) um HTML)
  const [item, setItems] = useState<itemType[]>([])

  const updateItems = () => {
    todosItems()
      .then(response => {
        setItems(response.data.data)
      })
      .catch((error) => {
        message.error('Erro ao carregar livros' + error)
      })  
  }

  const deletarItem = (id: number) => {
    deleteItem(id)
    .then(_response => {
      message. success('Livro deletado com sucesso!')
      updateItems()
    })
    .catch(error => {
      message.error("Erro ao deletar livro" + error)
    })
    updateItems
  }

  useEffect(() => {
    updateItems()
  }, [])
  
  return (                                                             //dentro do return é "onde fica o HTML", que usa os scripts criador na função (o return faz parte da função, btw)
    <Layout className='layout'>                                       {/* definindo className='layout, todo o layout vai usar as definições declaradas na classe layout do arquivo App.css */}
      <Header>
        Header 
      </Header>

      <Content>
        <Row justify='start' gutter={[15, 15]} style={{padding: '1rem'}}>
          {item.map((item: itemType) =>
            <Col span={6}> 
              <Card 
                actions={[
                  <Popconfirm
                    title={"Tem certeza que deseja deletar?"}
                    onConfirm={() => deletarItem(item.id!)}
                    okText="Sim"
                    cancelText="Não"
                  >
                    <div style={{ color: 'red' }}> <DeleteOutlined/> Deletar</div>
                  </Popconfirm>
                ]} 
                title={<p className='nome'>{item.nome}</p>} 
                hoverable>
                <p className='preco'>Preço: R${item.preco}</p> 
                <p className='categoria'>Categoria: {item.categoria}</p> 
                <p className='tempo'>Tempo de uso: {item.tempo} anos</p> 
              </Card>
            </Col>
          )}
          <ButtonAdd updateItems={updateItems}/>
        </Row>
      </Content>
      <Footer>
        Footer
      </Footer>
    </Layout>
  );
}

export default App      //exporta toda a função com o return sempre que chamar o "App"
