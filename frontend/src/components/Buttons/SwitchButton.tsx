import styles from "./SwitchButton.module.css";
import PS from "/PS.svg";
import PC from "/MOUSE.svg";

import { IButtonsClicked } from "../Body/Body";

type computerPlace = "PS" | "PC";

interface ISwitchButtonProps {
  type: computerPlace;
  buttonsClicked: IButtonsClicked;
  setButtonsClicked: (buttonsClicked: IButtonsClicked) => void;
}

const typeToImage = {
  PS: PS,
  PC: PC,
};

export function SwitchButton({
  type,
  buttonsClicked,
  setButtonsClicked,
}: ISwitchButtonProps) {
  const toggleAllButtons = () => {
    if (buttonsClicked[type] === true) return;
    const newButtonsClicked = Object.fromEntries(
      Object.entries(buttonsClicked).map(([key, value]) => [key, !value])
    );
    setButtonsClicked(newButtonsClicked);
  };

  return (
    <button className={styles.SwitchButton} onClick={toggleAllButtons}>
      <div className={styles.imageContainer}>
        <img
          src={typeToImage[type]}
          alt={type}
          className={
            buttonsClicked[type] === true
              ? styles.imageContainerClicked
              : styles.imageContainer
          }
        />
      </div>
    </button>
  );
}
