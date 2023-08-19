import { Col, Card, Modal, Form, Input, InputNumber, Button, Select, message } from 'antd'
import { PlusOutlined } from "@ant-design/icons";
import './addButton.css'
import { useState } from "react"
import { itemType } from "../../types/itemType";
import { criarItem } from "../../services/apiFunctions";

interface updateItemsProps {
    updateItems: () => void
}

const AddButton = ({ updateItems }: updateItemsProps) => {
    
    const [itemModalVisible, setItemModalVisible] = useState(false)

    const handleAdd = () => {
        setItemModalVisible(true)
    }

    function closeModal() {
        setItemModalVisible(false)
    }

    function onSubmit (values: itemType) {
        //
        //Provisório:
        const test = {
            nome: values.nome,
            preco: values.preco,
            categoria: values.categoria,
            tempo: values.tempo,
            id_user: 1
        }
        //
        //
        criarItem(test)
        .then(_response => {
            message.success(values.nome + 'Adicionado com sucesso!')
            updateItems()
        })
        .catch(error => {
            message.error('Erro ao adicionar o item!' + error)
        })
        closeModal()
    }

    const opcoes=[
        {label: 'Tecnologia', value: 'Tecnologia'},
        {label: 'Mobília', value: 'Mobilia'},
        {label: 'Roupas', value: 'Roupas'},
        {label: 'Cama, mesa e banho', value: 'Cama, mesa e banho'},
        {label: 'Veículos', value: 'Veículos'},
    ]

    return (
        <>
            <Col span={6}>
                <Card onClick={handleAdd} className='addBotao' hoverable>
                    <PlusOutlined style={{ fontSize: '1.5rem' }} />
                </Card>
            </Col>
            <Modal open={itemModalVisible} footer={false} onCancel={closeModal}> 
                <Form layout="vertical" onFinish={onSubmit}>
                    <Form.Item label='Nome do item' name={'nome'} rules={[{ required: true, message: 'O produto precisa ter um nome!'}]}>
                        <Input />
                    </Form.Item>

                    <Form.Item label='Preço' name={'preco'} rules={[{ required: true, message: 'O produto precisa ter um preço!'}]}>
                        <InputNumber controls={true} />
                    </Form.Item>

                    <Form.Item label='Categoria' name='categoria' rules={[{ required: true, message: 'O produto precisa ter uma categoria!'}]}>          
                        <Select style={{ width: '100%' }} options={opcoes} />
                    </Form.Item>

                    <Form.Item label='Tempo de uso' name={'tempo'} rules={[{ required: true, message: 'O produto precisa ter um tempo de uso!'}]}>
                        <InputNumber controls={true} />
                    </Form.Item>

                    <div>
                        <Button danger type='primary' onClick={closeModal}> Cancelar </Button>
                        <Button type='primary' htmlType="submit"> Submit </Button>
                    </div>
                </Form>
            </Modal>
        </>
    );
}

export default AddButton;