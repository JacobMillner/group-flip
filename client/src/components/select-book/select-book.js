import React from "react";
import "./select-book.css";
import { Card, Row } from "antd";
const { Meta } = Card;

function SelectBook() {
  return (
    <div>
      <Row type="flex" justify="space-around">
        <Card
          className="card"
          hoverable
          style={{ width: 240 }}
          cover={<img alt="example" src="/Viking-Pot-CT1.jpg" />}
        >
          <Meta title="Viking Pot" />
        </Card>
      </Row>
    </div>
  );
}

export default SelectBook;
