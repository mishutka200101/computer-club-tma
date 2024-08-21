import styles from "./PSCardButton.module.css";
import PS5Icon from "/PS5.svg";

import { TButtonClicked } from "../PSCard/PSCard.tsx";
import { Modal } from "../Modal/Modal.tsx";

import React, { useState } from "react";

interface IPSCardButton {
  text: TButtonClicked;
  buttonClicked: TButtonClicked;
  setButtonClicked: (button: TButtonClicked) => void;
}

export function PSCardButton({
  text,
  buttonClicked,
  setButtonClicked,
}: IPSCardButton) {
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const currentButtonClicked = buttonClicked && buttonClicked === text;

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.stopPropagation();
    setButtonClicked(text);
    setIsModalOpen(true);
  };

  return (
    <>
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        <h1>Hello</h1>
      </Modal>
      <button
        className={
          currentButtonClicked
            ? `${styles.PSCardButton} ${styles.Clicked}`
            : styles.PSCardButton
        }
        onClick={handleClick}
      >
        <img src={PS5Icon} alt={PS5Icon} />
        {text}
      </button>
    </>
  );
}
