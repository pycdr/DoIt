import React from "react";
import { Space, Row, Col, Modal, Collapse, Card, Button, Image, Skeleton } from "antd";
import { EyeOutlined } from "@ant-design/icons";
import PageSelector from "./PageSelector.js";
const { Panel } = Collapse;

class Months extends React.Component {
	constructor(props){
		super(props);
		this.data = props.data;
		this.readyMonths = {};
		this.state = {};
		this.data.map(x => {
			this.state[Number(x["@number"])]=false;
			this.readyMonths[Number(x["@number"])] = x
		});
		console.log(this.readyMonths);
	}
	render(){
		return (
			<Space wrap>
			{[0,1,2,3].map(x => (
				<><Row  gutter={[12, 8]}>
				{[x*3+1, x*3+2, x*3+3].map(y => (
					<Col span={8} style={{width:"33.33vw"}}>
						{!(y in this.readyMonths)?(
						<Skeleton />
						):(
						<Card
							title={this.readyMonths[y]["@name"]}
							extra={
							<Button
								icon={<EyeOutlined />}
								onClick={()=>{
									this.state[y] = true;
									this.setState(this.state);
								}}
							>show</Button>
							}
						>
							<Modal
								title={"details for month "+this.readyMonths[y]["@name"]}
								visible={this.state[y]}
								width="80vw"
								onOk={()=>{
									this.state[y] = false;
									this.setState(this.state);
								}}
								onCancel={()=>{
									this.state[y] = false;
									this.setState(this.state);
								}}
							>
							{Object.keys(this.readyMonths[y]).map(z => {
								if (z[0]!=="@") return <PageSelector data={{day:this.readyMonths[y][z]}} />
							})}
							</Modal>
							{this.readyMonths[y]["@image"]==undefined?(
							<Skeleton.Image />
							):(
							<Image src={this.readyMonths[y]["@image"]} height="20vw"/>
							)}
						</Card>)}
					</Col>
				))}
				</Row><br /></>
			))}
			</Space>
		);
	}
}
export default Months;
